#!/usr/lib/env python
# -*- coding:utf-8 -*-
import sys,urllib,re,time
import urllib.request
from bs4 import BeautifulSoup
import os

global num
num=0
i=0
def getURL(n):
    with urllib.request.urlopen('http://pic.yesky.com/c/6_4135_%d.shtml'%n,None,timeout=10) as url:    
        data=url.read()
        #"/uploadImages/2014/325/56/3BP7HM4218QR_160x120.jpg"
        #http://pic.yesky.com/uploadImages/2014/325/56/3BP7HM4218QR_160x120.jpg        
        #r=re.compile(r'http://pic.yesky.com/uploadImages/[a-z0-9-]{4}/[a-z0-9-]{3}/[a-z0-9-]{2}/[a-z0-9-]{12}_160x120.jpg')
        #pic=r.findall(data)
        ContentSoup = BeautifulSoup(data)
        pic = ContentSoup.find_all('img')
        return pic
 
for pageNo in range(1,5):
    picUrls=getURL(pageNo)
    length=len(picUrls)
    print(length)
    for i in range(0,length):
        try:
            print('get page:' + str(picUrls[i]))
            x = picUrls[i];
            x = x.get('src');
            print(x)
            if "160x120" or '180x135' in x:
                if not x.startswith('http'): x = 'http://pic.yesky.com' + x #相对路径补全
                print(x)
                if not os.path.exists('./pic2/%d.jpg'%num):
                    try:
                        picUrl=urllib.request.urlopen(x,None, timeout=3)
                        picContent=picUrl.read()
                        f=open('./pic2/%d.jpg'%num,'wb')
                        f.write(picContent)
                        f.close()
                    except Exception as e:
                        print(str(e))
                    time.sleep(1) 
                else:
                    print('./pic2/%d.jpg already exists' %num )
            print(num)
            num=num+1           
        except Exception as e:
            print(str(e))
print('Good Bye!')