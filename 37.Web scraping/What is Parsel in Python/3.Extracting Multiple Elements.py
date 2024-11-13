from parsel import Selector

html_content = """
<html>
    <body>
        <ul>
            <li>Geek 1</li>
            <li>Geek 2</li>
            <li>Geek 3</li>
        </ul>
    </body>
</html>
"""

selector = Selector(text=html_content)

# Using XPath
items = selector.xpath('//li/text()').getall()
print(items)

# Using CSS Selectors
items = selector.css('li::text').getall()
print(items)
