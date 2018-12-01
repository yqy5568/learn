# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

cursor = db.cursor()
class JingdongPipeline(object):
    def __init__(self):
        self.Coon = pymysql.connect(
        user='root',
        password='123123',
        db='jingdong',
        charset='utf8',
        host='localhost'
        )

    def process_item(self, item, spider):
        return item