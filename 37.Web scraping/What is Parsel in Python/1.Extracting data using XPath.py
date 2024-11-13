from parsel import Selector

html_content = """
<html>
    <body>
        <div class="content">
            <h1>Title: Extracting text using Xpath</h1>
            <p class="description">This is a description.</p>
        </div>
    </body>
</html>
"""

selector = Selector(text=html_content)
title = selector.xpath('//h1/text()').get()
print(title)
