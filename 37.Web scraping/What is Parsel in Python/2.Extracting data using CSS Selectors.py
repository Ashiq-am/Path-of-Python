from parsel import Selector

html_content = """
<html>
    <body>
        <div class="content">
            <h1>Title: Extracting text using Xpath</h1>
            <p class="description">GeeksForGeeks is a learning platform</p>
        </div>
    </body>
</html>
"""
selector = Selector(text=html_content)
description = selector.css('p.description::text').get()
print(description)
