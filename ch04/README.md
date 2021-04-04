# Chapter 4. Web Crawling Models

Although the applications of web crawlers are nearly endless, large scalable crawlers tend to fall into one of several patterns.

## Planning and Defining Objects

One of the best things you can do when deciding which data to collect is often to ignore the websites altogether.  It’s important to take a step back and perform a checklist for each item you consider and ask yourself the following questions:

- Will this information help with the project goals? Will it be a roadblock if I don’t have it, or is it just “nice to have” but won’t ultimately impact anything?
- If it might help in the future, but I’m unsure, how difficult will it be to go back and collect the data at a later time?
- Is this data redundant to data I’ve already collected?
- Does it make logical sense to store the data within this particular object? (As mentioned before, storing a description in a product doesn’t make sense if that description changes from site to site for the same product.)

If you do decide that you need to collect the data, it’s important to ask a few more questions to then decide how to store and handle it in code:
- Is this data sparse or dense? Will it be relevant and populated in every listing, or just a handful out of the set?
- How large is the data?
- Especially in the case of large data, will I need to regularly retrieve it every time I run my analysis, or only on occasion?
- How variable is this type of data? Will I regularly need to add new attributes, modify types (such as fabric patterns, which may be added frequently), or is it set in stone (shoe sizes)?

## Dealing with Different Website Layouts

- Create classes or reusable functions to make crawlers more flexible

## Structuring Crawlers

### Crawling sites through search
Looping through all topics first is a way to more evenly distribute the load placed on any one web server. This is especially important if you have a list of hundreds of topics and dozens of websites.

### Crawling sites through links
This type of crawler works well for projects when you want to gather all the data from a site - not just data from a specific search result or page listing. It also works well when the site’s pages may be disorganized or widely dispersed.

### Crawling multiple page types
Crawling through all internal links on a website can present a challenge in that you never know exactly what you’re getting.

There are a few basic ways to identify the page type:
- By the URL: All blog posts on a website might contain a URL (http://example.com/blog/title-of-post, for example).
- By the presence or lack of certain fields on a site: If a page has a date, but no author name, you might categorize it as a press release. If it has a title, main image, price, but no main content, it might be a product page.
- By the presence of certain tags on the page to identify the page: You can take advantage of tags even if you’re not collecting the data within the tags. Your crawler might look for an element such as <div id="related-products"> to identify the page as a product page, even though the crawler is not interested in the content of the related products.
