# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from main.models import ScrapyItem, Quote
import json

""" class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        item = ScrapyItem()
        item.unique_id = self.unique_id
        item.data = json.dumps(self.items)
        item.save()

    def process_item(self, item, spider):
        self.items.append(item['url'])
        return item


class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        quote = Quote(text=item.get('text'), author=item.get('author'))
        quote.save()
        return item """

from movie.models import Movie

def clean_title(param):
    return param

def clean_critics_consensus(param):
    return ' '.join(param)

def clean_average_grade(param):
    param = param.strip().replace('/5', '')
    return param

def clean_poster(param):
    if param:
        param = param[0]['path']
    return param

def clean_amount_reviews(param):
    return param.strip()

def clean_approval_percentage(param):
    return param.strip().replace('%', '')


class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        title = clean_title(item['title'])
        critics_consensus = clean_critics_consensus(item['critics_consensus'])
        average_grade = clean_average_grade(item['average_grade'])
        poster = clean_poster(item['images'])
        amount_reviews = clean_amount_reviews(item['amount_reviews'])
        approval_percentage = clean_approval_percentage(item['approval_percentage'])

        Movie.objects.create(
            title=title,
            critics_consensus=critics_consensus,
            average_grade=average_grade,
            poster=poster,
            amount_reviews=amount_reviews,
            approval_percentage=approval_percentage,
        )

        return item