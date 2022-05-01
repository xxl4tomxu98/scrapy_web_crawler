import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScrapyCrawlerSpider(CrawlSpider):
    name = 'scrapy_crawler'
    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        ScrapycrawlerSpider.rules = [
           Rule(LinkExtractor(unique=True), callback='parse_item'),
        ]
        super(IcrawlerSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item = {}
        item['url'] = response.url
        return item

    