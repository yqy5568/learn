# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
import re
from ..items import Uav81Item

class WangyiSpider(CrawlSpider):
    name = "wangyi"
    # allowed_domains = ["www"]
    # start_urls = ['http://temp.163.com/special/00804KVA/cm_guonei.js?callback=data_callback']
    def start_requests(self):
        for i in range(2,6):
            url = 'http://temp.163.com/special/00804KVA/cm_guonei_0'+ str(i) +'.js?callback=data_callback'
            yield scrapy.Request(url,self.parse_item)

    def parse_item(self, response):
        detail_url = re.findall('"docurl":"(.*?)"',response.text)
        for url in detail_url:
            # print(url)
            yield scrapy.Request(url,self.pars)

    def pars(self,response):
        try:
            #标题
            if response.xpath('//title/text()').extract_first():
                title = response.xpath('//title/text()').extract_first()
            else:
                raise Exception('title null')
            #发布时间
            if response.xpath('//div[@class="post_time_source"]/text()').extract_first():
                post_time = response.xpath('//div[@class="post_time_source"]/text()').extract_first().strip()[:19]
            else:
                raise Exception('time bull')
            #来源
            if response.xpath('//*[@id="ne_article_source"]/text()').extract_first():
                from_lai = response.xpath('//*[@id="ne_article_source"]/text()').extract_first()
            else:
                from_lai = ''
            #作者
            if response.xpath('//*[@id="endText"]/div[2]/span[2]/text()').extract_first():
                author = response.xpath('//*[@id="endText"]/div[2]/span[2]/text()').extract_first()
            else:
                author = ''
            #关键字
            if response.xpath('//meta[@name="keywords"]/@content').extract_first():
                keywords = response.xpath('//meta[@name="keywords"]/@content').extract_first()
            else:
                keywords = ''
            #导读
            if response.xpath('//meta[@name="description"]/@content').extract_first():
                description = response.xpath('//meta[@name="description"]/@content').extract_first()
            else:
                description = ''
            #正文
            if response.xpath('//*[@id="endText"]/p/text()').extract_first():
                content = ''.join(response.xpath('//*[@id="endText"]/p/text()').extract()).strip()
            else:
                content = ''
            #图片
            if response.xpath('//*[@id="endText"]/p/img/@src').extract():
                img_url = response.xpath('//*[@id="endText"]/p/img/@src').extract()
                print(img_url)
            else:
                img_url = ''
            item = Uav81Item()
            item['url'] = response.url
            item['title'] = title
            item['post_time'] = post_time
            item['from_lai'] = from_lai
            item['author'] = author
            item['keywords'] = keywords
            item['description'] = description
            item['content'] = content
            item['img_url'] = img_url
            yield item
        except Exception as e:
            print('error')
