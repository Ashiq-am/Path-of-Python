import io
import PyPDF2
import urllib.request
import scrapy
from scrapy.item import Item


class ParserspiderSpider(scrapy.Spider):
    name = 'parserspider'

    # URL of the pdf file.
    start_urls = ['https://codex.cs.yale.edu/avi\
	/os-book/OS9/practice-exer-dir/index.html']

    # default parse method
    def parse(self, response):
        # getting the list of URL of the pdf
        pdfs = response.xpath('//tr[3]/td[2]/a/@href')

        # Extracting the URL
        URL = response.urljoin(pdfs[0].extract())

        # calling urllib to create a reader of the pdf url
        File = urllib.request.urlopen(URL)
        reader = PyPDF2.pdf.PdfFileReader(io.BytesIO(File.read()))

        # creating data
        data = ""
        for datas in reader.pages:
            data += datas.extractText()

        print(data)
