import feedparser
from newspaper import Article

file_name = "rss_list.txt"
with open(file_name) as f:
    rss_urls = f.readlines()

rss_urls = [x.strip() for x in rss_urls]

for rss_url in rss_urls:
    feeds = feedparser.parse(rss_url)

    urls = [entry['link'] for entry in feeds['entries']]

    # print(urls)

    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        print(article.title)
