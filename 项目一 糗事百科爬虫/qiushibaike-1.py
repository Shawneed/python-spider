# -*- coding: utf-8 -*-
from lxml import etree
import requests

urls = []
for page in range(1, 10, 1):
	url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/?s=4866154'
	urls.append(url)

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}


for url in urls:
	html = requests.get(url, headers=head)
	selector = etree.HTML(html.text)
	content = selector.xpath('//div[@class="article block untagged mb15"]')

	for each in content:
		duanzi = each.xpath('div[2]/text()')
		answer = duanzi[0].encode('utf-8')
		print answer
