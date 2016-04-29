# -*- coding: utf-8 -*-

from lxml import etree
import requests
import re

url = 'http://www.jyb.cn/'
html = requests.get(url)
selector = etree.HTML(html.text)
headlines = selector.xpath('/html/body/div/div/div/div[@class="headlines"]')

for headline in headlines:
	headline_urls = headline.xpath('p/a/@href')
	
	headline_html = requests.get(headline_urls[0])

	headline_selector = etree.HTML(headline_html.content)
	titles = headline_selector.xpath('//*[@id="body"]/h1/text()')
	f = open('test.txt', 'a')
	for title in titles:
		f.write(title.encode('utf-8'))
		f.write('\n')
	
	documents = re.findall('<P>(.*?)</P>', headline_html.content, re.S)
	for document in documents:
		f.write(document.decode('gbk','ignore').encode('utf-8'))
	f.write('\n')
	f.write('\n')
	f.close()

	for headline_url in headline_urls[1:2]:
		headline_html = requests.get(headline_url)
		headline_selector = etree.HTML(headline_html.content)
		titles = headline_selector.xpath('//*[@id="body"]/h1/text()')
		f = open('test.txt', 'a')
		for title in titles:
			f.write(title.encode('utf-8'))
			f.write('\n')

		documents = re.findall('<P>(.*?)</P>', headline_html.content, re.S)
		for document in documents:
			f.write(document.decode('gbk','ignore').encode('utf-8').replace('<STRONG>', '').replace('</STRONG>', '').replace('&nbsp;', ' '))
			f.write('\n')
		f.write('\n')
		f.write('\n')
		f.close()

	for headline_url in headline_urls[2:3]:
		headline_html = requests.get(headline_url)
		print headline_html.content.decode('gbk','ignore').encode('utf-8')
		headline_selector = etree.HTML(headline_html.content)
		titles = headline_selector.xpath('//*[@id="body"]/h1/text()')
		f = open('test.txt', 'a')
		for title in titles:
			f.write(title.encode('utf-8'))
			f.write('\n')

		documents = re.findall('<P class=Custom_UnionStyle>(.*?)</P>', headline_html.content, re.S)
		for document in documents:
			print document.decode('gbk','ignore').encode('utf-8')
			f.write(document.decode('gbk','ignore').encode('utf-8').replace('<STRONG>', '').replace('</STRONG>', '').replace('&nbsp;', ' ').replace('<FONT color=#800000>', ' ').replace('</FONT>', ' '))
			f.write('\n')
		f.write('\n')
		f.write('\n')
		f.close()

	for headline_url in headline_urls[3:]:
		headline_html = requests.get(headline_url)
		headline_selector = etree.HTML(headline_html.content)
		titles = headline_selector.xpath('//*[@id="body"]/h1/text()')
		f = open('test.txt', 'a')
		for title in titles:
			f.write(title.encode('utf-8'))
			f.write('\n')

		documents = re.findall('<P>(.*?)</P>', headline_html.content, re.S)
		for document in documents:
			f.write(document.decode('gbk','ignore').encode('utf-8').replace('<STRONG>', '').replace('</STRONG>', '').replace('&nbsp;', ' '))
			f.write('\n')
		f.write('\n')
		f.write('\n')
		f.close()