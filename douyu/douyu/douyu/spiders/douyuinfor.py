# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuItem

class DouyuinforSpider(scrapy.Spider):
    name = "douyuinfor"
    allowed_domains = ["www.douyu.com"]
    # start_urls = ['http://www.douyu.com/']

    def start_requests(self):
        for i in range(1,11):
            url = ''
            # print(url)
            yield scrapy.Request(url,self.parse)

    def parse(self, response):
        # print(response.url)
        data = json.loads(response.text).get('data').get('list')
        for item in data:
            infor = DouyuItem()
            infor['avatar'] = item.get('avatar')
            infor['hn'] = item.get('hn')
            infor['nickname'] = item.get('nickname')
            infor['rid'] = item.get('rid')
            infor['roomName'] = item.get('roomName')
            infor['verticalSrc'] = item.get('verticalSrc')
            # print(infor['avatar'],infor['hn'],infor['nickname'],infor['rid'],infor['roomName'],infor['verticalSrc'])
            yield infor
