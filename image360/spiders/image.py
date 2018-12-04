# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import Request
from urllib.parse import urlencode
from image360.items import ImageItem


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def start_requests(self):
        data = {'ch': 'photography', 't1': '225', 'listtype': 'new'}
        base_url = 'https://image.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            yield item
