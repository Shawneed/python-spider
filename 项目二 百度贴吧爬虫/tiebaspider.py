# -*- coding: utf-8 -*-
from lxml import etree
import requests

urls = []
for page in range(1, 5, 1):
	addr = 'http://tieba.baidu.com/p/3138733512?see_lz=1&pn=' + str(page)
	urls.append(addr)

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}

html1 = requests.get(urls[0], headers=head)
title = etree.HTML(html1.text).xpath('//*[@id="j_core_title_wrap"]/h3/@title')[0]
print title.encode('utf-8')

for url in urls:
	html = requests.get(url, headers=head)
	html_content = etree.HTML(html.text).xpath('//*[@id="j_p_postlist"]/div[@class="l_post l_post_bright j_l_post clearfix  "]')

	for each in html_content:
		content = each.xpath('div/div/cc/div[@class="d_post_content j_d_post_content "]')[0]
		content_1 = content.xpath('string(.)')
		print content_1.encode('utf-8')

		content = each.xpath('div/div/cc/div/text()')[0].encode('utf-8')
		print content
