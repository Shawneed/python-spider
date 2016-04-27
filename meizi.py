# -*- coding: utf-8 -*-

'''
Script Name     : meizi.py
Author          : winson
Created         : 2015-04-23
Description     : 网站爬取图片
'''

import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}

"""
Description    : 将网页图片保存本地
@param imgUrl  : 待保存图片URL
@param imgName : 待保存图片名称
@return 无
"""
def saveImage( imgUrl,imgName ="default.jpg" ):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    DstDir="C:\\Users\\Winson\\Desktop\\meizi\\"
    print("保存文件"+DstDir+imgName+"\n")
    try:
        with open(DstDir+imgName ,"wb") as jpg:
            jpg.write(image)     
            return
    except IOError:
        print("IO Error\n")
        return
    finally:
        jpg.close   


def getweblist():
	urls = []
	for i in range(1500, 1664, 1):
		url = 'http://jandan.net/ooxx/page-{}#comments'.format(i)
		urls.append(url)
	return urls     

        
"""
Description    : 获取图片地址
@param pageUrl : 网页URL
@return : 图片地址列表
"""

def getfilelist(pageUrl):
    web = requests.get(pageUrl, headers = header)
    soup = BeautifulSoup(web.text, 'lxml')
    filelist=[]
    for photo in soup.select('#comments img'):
        filelist.append(photo.get('src'))
    return filelist


if __name__ == "__main__":
  num = 0
  list = getweblist()
  for page in list:
    imagelist = getfilelist(page)
    for file in imagelist:
	    saveImage(file, str(num) + '.jpg')
	    num += 1
