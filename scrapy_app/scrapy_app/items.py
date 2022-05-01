# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from movie.models import Movie

class MovieItem(DjangoItem):
    django_model = Movie
    image_urls = scrapy.Field()
    images = scrapy.Field()

class ScrapyAppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
