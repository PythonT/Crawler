#!/usr/bin/env python
#coding:utf-8
'''
an Simple example.
To ：https://github.com/hustcc/object2json
@author: tyler.yan
@contact: qq:156926528

use Request && BeautifulSoup

Request
https://github.com/kennethreitz/requests
wget 'https://github.com/kennethreitz/requests/archive/master.zip'
python setup.py install

BeautifulSoup
http://www.crummy.com/software/BeautifulSoup/bs4/download/4.3/beautifulsoup4-4.3.2.tar.gz

Created on 2014年11月28日
'''

import requests
from bs4 import BeautifulSoup
import re
import urllib
import time
import os

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 10#default timeout

PhotoName = 0
c = '.jpeg'
PATH="./pic/"
for x in range(1,4):  
  site =  "http://bbs.meizu.cn/forum-62-%d.html" %x  
  print("start page:" + str(site))
  Page = requests.session().get(site,headers=head,timeout=TimeOut)
  Coding =  (Page.encoding)
  Content = Page.content  #.decode(Coding).encode('utf-8')
  ContentSoup = BeautifulSoup(Content)
  #jpg = ContentSoup.find_all('img',{'class':'scrollLoading'})
  jpg = ContentSoup.find_all('img',{'isdrift':'true'})
  for photo in jpg:
    try:
      #print('photo address:' + str(photo))
      picURL = photo.get('src')#获取头像链接
      #print('photoAdd:' + str(picURL))
      PhotoName +=1
      Name =  (str(PhotoName)+c)
      print("[" + str(x) + "]name:" + Name +",url:" + picURL)
      r = requests.get(picURL,stream=True)#获取图片内容
      storeFilePath = PATH+Name
      print('storeFilePath:' + str(storeFilePath))
      if not os.path.exists(storeFilePath):
        print(str(storeFilePath) + " not exist!")
        with open(storeFilePath, 'wb') as fd:
                  for chunk in r.iter_content():
                      fd.write(chunk)
              #print("Thread sleep 1 Second!")        
      else:
        print(str(storeFilePath) + " already exist!")
      time.sleep(1);
    except Exception as e:
      print(str(e))
  print("end page:" + str(site))       
  
print ("You have down %d photos" %PhotoName)