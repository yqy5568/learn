# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import Uav81Item

class FeijiSpider(CrawlSpider):
    name = 'feiji'
    allowed_domains = []
    start_urls = [
        'http://www.81uav.cn/uav-news/4.html'
    ]

    rules = (
        Rule(LinkExtractor(allow='http://www.81uav.cn/uav-news/4_\d+.html',),follow=True),
        Rule(LinkExtractor(allow="http://www.81uav.cn/uav-news/\d{6}/\d{2}/\d+.html", restrict_css="div.news_left a"),callback="parse_item", follow=False),
    )

    def parse_item(self, response):
            # print(response.url)
        try:
            sel = Selector(response)
            # 标题
            if sel.xpath("//h1/text()").extract_first():
                title = sel.xpath("//h1/text()").extract_first()
                # print(title)
            else:
                raise Exception('title null')
                # print(response.url)
            # print(title)
            # 时间
            if sel.css("div.info::text").re("\d{4}-\d{2}-\d{2}"):
                post_time = sel.css("div.info::text").re("\d{4}-\d{2}-\d{2}")[0]
            else:
                raise Exception('time null')
            # print(date)
            # 正文
            if sel.xpath('//div[@id="article"]/p/text()').extract():
                content = ';'.join(sel.xpath('//div[@id="article"]/p/text()').extract())
            else:
                content = ''
            # print(content)
            # 关键词
            if sel.xpath('//div[@class="view"]/div[8]/a/text()').extract_first():
                keyword = sel.xpath('//div[@class="view"]/div[8]/a/text()').extract_first()
            else:
                keyword = ''
            # print(keyword)
            # 链接
            if sel.xpath('//div[@class="view"]/div[6]/a/text()').extract_first():
                url = sel.xpath('//div[@class="view"]/div[6]/a/text()').extract_first()
            else:
                url = ''
            # print(url)
            # 图片
            if sel.xpath('//div[@id="article"]/p/img/@src').extract():
                img_url = sel.xpath('//div[@id="article"]/p/img/@src').extract()
            else:
                img_url = ''
            # 导读
            if response.xpath('//meta[@name="description"]/@content').extract_first():
                description = response.xpath('//meta[@name="description"]/@content').extract_first()
            else:
                description = ''
            # print(pic)
            item = Uav81Item()
            item['title'] = title
            item['post_time'] = post_time
            item['content'] = content
            item['keyword'] = keyword
            item['url'] = url
            item['img_url'] = img_url
            item['description'] = description
            # print(item)
            yield item
        except Exception as e:
            print('error')

