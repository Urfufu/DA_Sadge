import scrapy
class SadgeSpider(scrapy.Spider):
    name = "SadgeSpider"
    start_urls = ['http://192.168.50.58/algenius']

    def parse(self, response):
        for x in response.css('img'):
            yield {
                'Image Link': x.xpath('@src').extract_first(),
            }
