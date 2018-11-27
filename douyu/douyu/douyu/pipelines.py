# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib import request
import pymongo
import redis
import pymysql

class DouyuPipeline(object):
    def __init__(self):
        self.rd = redis.Redis(db=0)
        self.MC = pymongo.MongoClient('localhost')
        self.DB = self.MC.douyu
        self.My_Collection = self.DB.infor
        self.mysql_conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'benjamin',
            db = 'douyu',
            charset = 'utf8'
        )
        self.cur = self.mysql_conn.cursor()

    def process_item(self, item, spider):
        path = './img'
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)

        # request.urlretrieve(item['verticalSrc'],path+'/'+item['nickname']+'.jpg')

        # self.My_Collection.insert(dict(item))
        # self.rd.set(item['nickname'],dict(item))

        sql_str = 'insert into douyu(avatar,hn,nickname,rid,roomName,verticalSrc) values(%s,%s,%s,%s,%s,%s)'
        tp = (item['avatar'],item['hn'],item['nickname'],item['rid'],item['roomName'],item['verticalSrc'])
        self.cur.execute(sql_str,tp)
        self.mysql_conn.commit()
        return item
