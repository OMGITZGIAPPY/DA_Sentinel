# Scrapy Case
import scrapy
# Classification Name ZipperSpider
class ZipperSpider(scrapy.Spider):

    name = "Zipper_spider" # Name of the spider
    start_urls = ['http://192.168.10.101/zipper/'] # The URL to start the scraping
    # Function of ZipperSpider
    def parse(self, response):
            # To select only image files
            css_selector = 'img'
            # To select and extract the link file out.
            for x in response.css(css_selector):
                newsel = '@src'
                yield {
                    'JPG Link': x.xpath(newsel).extract_first(),
                }