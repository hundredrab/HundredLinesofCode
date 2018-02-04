# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['genius.com']
    start_urls = ['http://genius.com/']

    def parse(self, response):
        pass
