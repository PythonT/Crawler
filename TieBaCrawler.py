#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib.request
import sys,re
import time
from queue import Queue
#import thread
import threading
#import jieba
#import chardet
from bs4 import BeautifulSoup
 
DEEP = 1000
LOCK = threading.Lock()
PATH = "c:\\test\\"

urlQueue = Queue()#链接队列

def getPageUrl(html):
  #print(html)
  if  not html is None :    
    reUrl = re.compile(r'<\s*[Aa]{1}\s+[^>]*?[Hh][Rr][Ee][Ff]\s*=\s*[\"\']?([^>\"\']+)[\"\']?.*?>')
    urls = reUrl.findall(html)#html is bytes!
    for url in urls:
      if len(url) > 10:
        if url.find('javascript') == -1:
          print('find new url ' + str(url))
          urlQueue.put(url) 
     
def getContents(url):
  try:
    url = urllib.request.quote(url.split('#')[0].encode('utf-8'), safe = "%/:=&?~#+!$,;'@()*[]")
    req = urllib.request.urlopen(url,none,timeout=5)
    res = req.read()
    #code = chardet.detect(res)['encoding']        
    #res = res.decode(str(code), 'ignore')
    #res = res.encode('gb2312', 'ignore')
    #code = chardet.detect(res)['encoding']        
    return res.decode()
  except urllib.request.HTTPError as e:
    print(e.code)
    return None
  except urllib.request.URLError as e:
    print(e)
    return None
  except:
    print('Other exception !')
    return None

def writeToFile(html, url):
  fp = file(PATH + str(time.time()) + '.html', 'w')
  fp.write(html)
  fp.close()
 
def getKeyWords(html):
  #code = chardet.detect(html)['encoding']
  #if code == 'ISO-8859-2':
    #html.decode('gbk', 'ignore').encode('gb2312', 'ignore')
    #code = chardet.detect(html)['encoding']
    #soup = BS(html, fromEncoding="gb2312")
    soup = BeautifulSoup(html)     
    titleTag = soup.title
    titleKeyWords = titleTag.contents[0]
    cutWords(titleKeyWords)

def cutWords(contents):
  print(contents)
  #print contents
  #res = jieba.cut_for_search(contents)
  #res = '\n'.join(res)
  #print res
  #res = res.encode('gb2312')
  #keyWords = file(PATH + 'cutKeyWors.txt', 'a')
  #keyWords.write(res)
  #keyWords.close()

def start_crawl():
  while urlQueue.empty() == False:
    url = urlQueue.get()
    print('start url ' + str(url))
    html = getContents(url)
    getPageUrl(html)
    getKeyWords(html)
    #writeToFile(html, url) 
  else:
    print('queue empty ,Good Bye!')
if __name__ == '__main__':
  urlQueue.put('http://www.baidu.com' )
  start_crawl() 
 