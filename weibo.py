#-*-coding:utf8-*-

import requests
from lxml import etree
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def saveImage( imgUrl,imgName ="default.jpg" ):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    DstDir="C:\\Users\\Winson\\Desktop\\weibo\\"
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

#防止编码错误
url_login = 'https://login.weibo.cn/login/'
html = requests.get(url_login).content
selector = etree.HTML(html)
password = selector.xpath('//input[@type="password"]/@name')[0]
vk = selector.xpath('//input[@name="vk"]/@value')[0]
action = selector.xpath('//form[@method="post"]/@action')[0]

print action
print password
print vk
print" ************* "

newurl = url_login + action
data = {
    'mobile' : 'xxx',
    password : 'xxx',
    'remember' : 'on',
    'backURL' : 'http://weibo.cn/',
    'backTitle' : u'手机新浪网',
    'tryCount' : '',
    'vk' : vk,
    'submit' : u'登录'
}



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}
cookie=requests.post(newurl, data).cookies
print cookie

newpage = 'http://weibo.cn/guosite?c=spr_qdhz_bd_baidusmt_weibo_s&nick=%E9%83%AD%E6%96%AF%E7%89%B9&is_hot=1'


html = requests.get(newpage, cookies = cookie, headers=headers).content
allurl = re.findall('<img src="(.*?)" alt=', html)
print allurl
num = 0
for url in allurl:
    saveImage(url, str(num)+'.jpg')
    num +=1

