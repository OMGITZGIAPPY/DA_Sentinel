import scrapy
class ZipperSpider(scrapy.Spider):
    name = "Zipper_spider"
    start_urls = ['http://192.168.10.101/zipper/']
    def parse(self, response):
            css_selector = 'img'
            for x in response.css(css_selector):
                newsel = '@src'
                yield {
                    'JPG Link': x.xpath(newsel).extract_first(),
                }