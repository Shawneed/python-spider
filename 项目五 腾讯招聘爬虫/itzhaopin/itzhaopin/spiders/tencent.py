# -*- coding: utf-8 -*-
import scrapy
import json
from itzhaopin.items import ItzhaopinItem
# from scrapy.http import Request

class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    start_urls = (
        'http://hr.tencent.com/position.php',
    )

    def start_requests(self):
        reqs=[]
        
        for i in range(0, 100, 10):
            req=scrapy.Request("http://hr.tencent.com/position.php?&start=%s#a"%i)
            reqs.append(req)
        
        return reqs

    def parse(self, response):
        content = response.xpath('//*[@id="position"]/div/table[@class="tablelist"]')
        items = []
        for each in content:
        	item = ItzhaopinItem()
        	item['name'] = each.xpath('tr/td/a/text()')[0].extract()
        	item['catalog'] = each.xpath('tr/td[2]/text()')[1].extract()
        	item['workLocation'] = each.xpath('tr/td[4]/text()')[1].extract()
        	item['recruitNumber'] = each.xpath('tr/td[3]/text()')[1].extract()
        	link = each.xpath('tr/td[1]/a/@href')[0].extract()
        	item['detailLink'] = 'http://hr.tencent.com/' + link
        	item['publishTime'] = each.xpath('tr/td[5]/text()')[1].extract()
        	items.append(item)
        return items