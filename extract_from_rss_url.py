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

for rss_url in rss_urls:
    feeds = feedparser.parse(rss_url)

    urls = [entry['link'] for entry in feeds['entries']]

    print(urls)

    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        print(article.title)

        fe = fg.add_entry()
        fe.id(url)
        fe.title(article.title)
        fe.link(href=url)
        fe.description(article.text)

output_file = "atom.xml"
fg.atom_file(output_file)
