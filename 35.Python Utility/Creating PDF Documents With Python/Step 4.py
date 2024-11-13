# registering a external font in python
pdfmetrics.registerFont(
	TTFont('abc', 'SakBunderan.ttf')
)

# creating the title by setting it's font
# and putting it on the canvas
pdf.setFont('abc', 36)
pdf.drawCentredString(300, 770, title)
