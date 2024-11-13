# returns title of the blog site
blog_feed.feed.title

# returns the link of the blog
# and number of entries(blogs) in the site.
blog_feed.feed.link
len(blog_feed.entries)

# Details of individual blog can
# be accessed by using attribute name
print(blog_feed.entries[0].title)
print(blog_feed.entries[0].link)
print(blog_feed.entries[0].author)
print(blog_feed.entries[0].published)

# Getting lists of tags and authors.
tags = [tag.term for tag in blog_feed.entries[0].tags]
authors= [author.name for author in blog_feed.entries[0].authors]
