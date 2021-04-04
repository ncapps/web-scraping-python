# Chapter 3: Writing Web Crawlers

The general approach to an exhaustive site crawl is to start with a top-level page (such as the home page), and search for a list of all internal links on that page. Every one of those links is then crawled, and additional lists of links are found on each one of them, triggering another round of crawling

## Handling Redirects
 If you’re using the requests library, make sure to set the allow-redirects flag to True:
 ```python
 r = requests.get('http://github.com', allow_redirects=True)
 ```