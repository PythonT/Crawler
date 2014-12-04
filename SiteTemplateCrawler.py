#!/usr/bin/env python
#coding:utf-8
import urllib
import urllib.request
import os,re
 
if __name__ == '__main__':
     
    pathw = os.getcwd()
 
    #图片和标题目录
    imagetitleregion = r'<div class="large-Imgs">\r\n                             <img src="(.+?)" alt="(.+?)">'
    imagetitlRe = re.compile(imagetitleregion)
 
    #提取文件
    downregion = '<a href="(.+?)" target="_blank" class="button btn-down" title="免费下载"><i class="icon-down icon-white"></i><i class="icon-white icon-down-transiton"></i>免费下载</a>'
    downRe = re.compile(downregion)
 
    for i in range(5, 5365 + 1):
        try:
            response = urllib.request.urlopen('http://www.cssmoban.com/cssthemes/'+str(i)+'.shtml') 
            html = response.read()
            print('爬'+str(i)+'页面数据')
             
            #提取图片和标题
            m = imagetitlRe.findall(html,re.S)
             
            imageurl = m[0][0].decode("utf-8")
            title = m[0][1].decode("utf-8")
            path = pathw+'\\'+title+'_'+str(i)
            #print imageurl
            if not(os.path.isdir(path)):
                os.mkdir(path)
 
            if imageurl != u'佚名':
                urllib.urlretrieve('http://www.cssmoban.com'+imageurl, path+'\\'+str(i)+'.jpg')
 
            #提取文件
            m = downRe.findall(html)
 
            urllib.urlretrieve(m[0], path+'\\'+str(i)+'.rar')
            print('爬'+str(i)+'页面数据完成')
        except Exception as e:  
            print('爬页面数据失败',e)