# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class Uav81Pipeline(object):
    def __init__(self):
        self.Conn = pymysql.connect(
            host = 'localhost',
            password = '123456',
            user = 'root',
            db = 'wangyi',
            charset = 'utf8'
        )
    def process_item(self, item, spider):
        cursor = self.Conn.cursor()
        sql = 'insert into infor(url,title,post_time,from_lai,author,keywords,description,content,img_url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        tp = (item['url'],item['title'],item['post_time'],item['from_lai'],item['author'],item['keywords'],item['description'],item['content'],item['img_url'])
        cursor.execute(sql,tp)
        self.Conn.commit()
        return item


