# -*- coding: utf-8 -*-
import scrapy
import re

class PepbookSpider(scrapy.Spider):
    name = 'pepbook'
    allowed_domains = ['bp.pep.com.cn']
    start_urls = ['http://bp.pep.com.cn/jc/']

    def parse(self, response):
        for link in response.xpath("//li[@class='fl']/a/@href"):
            yield response.follow(link.get(), self.parseBooks)

    def parseBooks(self, response):
        for book in response.xpath("//li[@class='fl']"):
            book_names = book.xpath("h6/a/text()").getall()
            filt = getattr(self, 'filt', None)
            if filt is not None:
                if not re.search(filt, book_names[0]):
                    continue
            paths = list(map(lambda x: response.urljoin(x), book.xpath("div/a[@class='btn_type_dl']/@href").getall()))
            yield {
                'file_names': book_names,
                'file_urls': paths
            }
        
