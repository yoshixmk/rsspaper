import feedparser
from newspaper import Article
from feedgen.feed import FeedGenerator
from datetime import datetime

file_name = "rss_list.txt"
with open(file_name) as f:
    rss_urls = f.readlines()

rss_urls = [x.strip() for x in rss_urls]

fg = FeedGenerator()
fg.id(datetime.now().strftime('%Y_%m_%d'))
fg.title('extract_from_rss_url')
fg.author({'name': 'yoshixmk'})
fg.language('ja')


strings_for_html = ["<!DOCTYPE html><html lang='ja'><meta http-equiv='content-type' charset='utf-8'><body style='display: table'>"]
for rss_url in rss_urls:
    feeds = feedparser.parse(rss_url)

    urls = [entry['link'] for entry in feeds['entries']]

    print(urls)

    for url in urls:
        article = Article(url)
        try:
            article.download()
            article.parse()
        except:
            import traceback
            traceback.print_exc()
            continue
        print(article.title)

        fe = fg.add_entry()
        fe.id(url)
        fe.title(article.title)
        fe.link(href=url)
        fe.description(article.text)
        strings_for_html.append("<b style='color:#00cc7e'>" + article.title + "</b><br>")
        strings_for_html.append(article.text + "<br>")

output_file = "public/atom.xml"
fg.atom_file(output_file)

strings_for_html.append("</body></html>")
with open("public/simple.html", "w", encoding="utf-8") as f:
    f.writelines(strings_for_html)
