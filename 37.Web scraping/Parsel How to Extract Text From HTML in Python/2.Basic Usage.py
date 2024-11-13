# Create a Selector object
selector = Selector(text=html_content)

# Extract data using CSS selectors
title = selector.css('title::text').get()
main_heading = selector.css('h1::text').get()
paragraphs = selector.css('p::text').getall()
div_content = selector.css('div.content').get()

# Print extracted data
print("Title:", title)
print("Main Heading:", main_heading)
print("Paragraphs:", paragraphs)
print("Div Content:", div_content)
