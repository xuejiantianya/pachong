# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import csv
import pymongo

# class MongoPipeline(object):
#
#     collection_name = 'scrapy_items'
#
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DATABASE')
#         )
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         # self.db[self.collection_name].insert_one(dict(item))
#         self.db['user'].update({'url_token':item['url_token']},{'$set':item},True)
#
#         return item



# import json
#
# class JsonWriterPipeline(object):
#
#     def open_spider(self, spider):
#         self.file = open('items.jl', 'w')
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item


class WangyinPipeline_a(object):
    def __init__(self):
        self.f = open("wangyiyun.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['id', 'name', 'avatar_url', 'headline','url','url_token'])

    def process_item(self, item, spider):
        wangyiyun_list =  [item['id'], item['name'], item['avatar_url'], item['headline'],item['url'], item['url_token']]

        self.writer.writerow(wangyiyun_list)
        return item
    def close_spider(self, spider):#关闭
        self.writer.close()
        self.f.close()