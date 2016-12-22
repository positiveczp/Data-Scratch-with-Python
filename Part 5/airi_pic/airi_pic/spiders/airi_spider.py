from scrapy.spiders import Spider
from scrapy.selector import Selector
from airi_pic.items import AiriPicItem

class AiriPicSpider(Spider):
    name = "airi"
    start_urls = [
        "http://tieba.baidu.com/p/4023230951"
    ]

    def parse(self, response):
        sel = Selector(response)
        image_url = sel.xpath("//div[@id='post_content_75283192143']/img[@class='BDE_Image']/@src").extract()
        item = AiriPicItem()
        item['airi_image_url'] = image_url

        yield item







































