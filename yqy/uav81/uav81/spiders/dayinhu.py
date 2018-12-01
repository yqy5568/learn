# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import re

class DayinhuSpider(CrawlSpider):
    name = "dayinhu"
    # allowed_domains = ["www"]
    start_urls = ['http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF']
    rules = (
        Rule(LinkExtractor(allow="http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/\d+.html", ), follow=True),
        Rule(LinkExtractor(allow="http://www.dayinhu.com/news/\d{6}.html", restrict_css="h1.entry-title a"),
             callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        #文章链接
        print(response.url)
        try:
            sel = Selector(response)
            #标题
            if sel.xpath('//h1/text()').extract_first():#False
                title = sel.xpath('//h1/text()').extract_first()
                print(title)
            else:
                raise Exception("title is null")
            #时间
            if sel.xpath('//time[@class="entry-date"]/text()').extract_first():
                date_time = sel.xpath('//time[@class="entry-date"]/text()').extract_first()
                print(date_time)
            else:
                raise Exception("date_time is null")
            #正文
            if sel.xpath('//div/p/text()').extract():
                content = ''.join(sel.xpath('//div/p/text()').extract())
                print(content)
            else:
                date_time = ''
            #关键字
            if sel.xpath('//meta[@name="keywords"]/@content').extract_first():
                keywords = sel.xpath('//meta[@name="keywords"]/@content').extract_first()
                print(keywords)
            else:
                keywords = ''
            #图片
            html = response.text
            img = re.compile('img src="(.*?)"',re.S)
            img_list = re.findall(img,html)
            img_url = img_list[1:]
            print(img_url)
            #导读
            if sel.xpath('//meta[@name="description"]/@content').extract_first():
                description = sel.xpath('//meta[@name="description"]/@content').extract_first()
                print(description)
            else:
                description = ''
        except Exception as e:
            print("ss")