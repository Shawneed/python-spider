# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class CollectipsPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        client = pymongo.MongoClient()
        tdb = client[settings['MONGODB_DBNAME']]
        self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
    	bookInfo = dict(item)
        self.post.insert(bookInfo)
        return item
