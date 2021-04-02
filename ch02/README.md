# Chapter 2: Advanced HTML Parsing

## Options to simplify a complex page
1. Look for a "Print This Page" link or a mobile version of the site
2. Look for information hidden in a JavaScript file
3. Information might be available in the URL of the page

## BeautifulSoup methods
`get_text()`: Strips all tags from the document and returns a Unicode string containing text only. It's much easier to find what you're looking for in a BS object than in a block of text. Calling `.get_text()` should be the last thing you do before printing, storing, or manipulating the data.
[`find_all()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all): Looks through a tag's descendants and retrieves all descendants that match your filters
[`find()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find): Find the first result based on your filters instead of scanning the entire document

```python
find_all(tag, attributes, recursive, text, limit, keywords)

find(tag, attributes, recursive, text, keywords)

.find_all('span', {'class':{'green', 'red'}})
```

## Keyword Arguments and "Class"
- `class` is a reserved word in python
```python
bs.find_all(class_='green')

bs.find_all('', {'class': 'green'})
```

## BeautifulSoup Objects
- BeautifulSoup objects
- Tag objects: Retrieved in lists, or retrieved individually by calling `find` and `find_all` on a BeautifulSoup object, or drilling down
- NavigableString: Used to represent text within tags, rather than the tags themselves
- Comment: Used to find HTML comments in comment tags, <!--like this one-->.

## Dealing with Children and Other Descendants
In the BeautifulSoup library, as well as many other libraries, there is a distinction drawn between children and descendants: much like in a human family tree, children are always exactly one tag below a parent, whereas descendants can be at any level in the tree below a parent.

## Regular Expressions
- “Let’s say you have a problem, and you decide to solve it with regular expressions. Well, now you have two problems.”
- When attempting to write any regular expression from scratch, it’s best to first make a list of steps that concretely outlines what your target string looks like.
- [regex playground](https://www.regexpal.com/)

```sh
# Regex for email addresses

[A-Za-z0-9._+]+@[A-Za-z]+.(com|org|edu|net)
```

### Commonly used regex symbols
Symbol(s) | Meaning | Example
--- | --- | ---
`*` | Matches the preceding character, subexpression, or bracketed character, 0 or more times. | `a*b*`
`+` | Matches the preceding character, subexpression, or bracketed character, 1 or more times. | `a+b+`
`[]` | Matches any character within the brackets (i.e., “Pick any one of these things”). | `[A-Z]*`
`()` | A grouped subexpression (these are evaluated first, in the “order of operations” of regular expressions). | `(a*b)*`
`{m,n}` | Matches the preceding character, subexpression, or bracketed character between m and n times (inclusive). | `a{2,3}b{2,3}`
`[^]` | Matches any single character that is not in the brackets. | `[^A-Z]*`
`\|` | Matches any character, string of characters, or subexpression, separated by the `\|` | `b(a\|i\|e)d`
`.` | Matches any single character (including symbols, numbers, a space, etc.). | `b.d`
`^` | Indicates that a character or subexpression occurs at the beginning of a string. | `^a`
`\` | \	An escape character (this allows you to use special characters as their literal meanings). | `\^ \\| \\`
`$` | $	Often used at the end of a regular expression, it means “match this up to the end of the string.” Without it, every regular expression has a de facto “.*” at the end of it, accepting strings where only the first part of the string matches. This can be thought of as analogous to the ^ symbol. | `[A-Z]*[a-z]*$`
`?!` | “Does not contain.” This odd pairing of symbols, immediately preceding a character (or regular expression), indicates that that character should not be found in that specific place in the larger string. This can be tricky to use; after all, the character might be found in a different part of the string. If trying to eliminate a character entirely, use in conjunction with a ^ and $ at either end. | `^((?![A-Z]).)*$`

## Accessing Attributes
```python
myImgTag.attrs['src']
```

## Lambda Expressions
-  A lambda expression is a function that is passed into another function as a variable
- The only restriction is that these functions must take a tag object as an argument and return a boolean.
- Every tag object that BeautifulSoup encounters is evaluated in this function, and tags that evaluate to True are returned, while the rest are discarded.

```python
# Find tags with 2 attributes

bs.find_all(lambda tag: len(tag.attrs) == 2)

# Use existing functions
bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
```
