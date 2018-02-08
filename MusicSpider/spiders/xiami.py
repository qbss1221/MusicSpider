# -*- coding: utf-8 -*-
import scrapy


class XiamiSpider(scrapy.Spider):
    name = 'xiami'
    allowed_domains = ['xiami.com']
    start_urls = ['http://www.xiami.com/']

    def parse(self, response):
        pass
