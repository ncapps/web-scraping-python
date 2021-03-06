# Chapter 5. Scrapy

Scrapy is one of the best frameworks for developing crawlers

```bash
scrapy runspider article.py
```

Scrapy also provides useful tools to keep your collected items organized and stored in custom objects with well-defined fields.

Although Scrapy is single threaded, it is capable of making and handling many requests asynchronously.


## The Item Pipeline
Scrapy’s item pipeline can improve the speed of your web scraper even further by performing all data processing while waiting for requests to be returned, rather than waiting for data to be processed before making another request.

## Logging with Scrapy
The debug information generated by Scrapy can be useful. You can easily adjust the level of logging by adding a line to the settings.py file in your Scrapy project.

## Tutorial notes
- [Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html#intro-tutorial)
- https://github.com/scrapy/quotesbot
- Spiders are classes that you define and that Scrapy uses to scrape information from a website
- Unlike `scrapy.Request`, `response.follow` supports relative URLs directly - no need to call urljoin.

```bash
$ cd tutorial
$ scrapy crawl quotes -O quotes.json
```
