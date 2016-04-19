# -*- coding: utf-8 -*-
from lxml import etree
import requests

urls = []
for page in range(1, 3, 1):
	url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/?s=4866154'
	urls.append(url)

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}


for url in urls:
	html = requests.get(url, headers=head)
	selector = etree.HTML(html.text)
	content = selector.xpath('//div[@class="article block untagged mb15"]')

	for each in content:
		try:
			name = each.xpath('div/a/@title | div/span/h2/text()')[0]
			print name.encode('utf-8')
		except:
			print '没有名字'

		duanzi_con = each.xpath('div[@class="content"]')[0]
		info = duanzi_con.xpath('string(.)')
		content_2 = info.replace('\n','').replace(' ','')
 		print content_2.encode('utf-8')

		good_num = each.xpath('div/span/i/text()')[0].encode('utf-8')
		print good_num,

		dot = each.xpath('div/span/span[@class="dash"]/text()')[0].encode('utf-8')
		print dot

