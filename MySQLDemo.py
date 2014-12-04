#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#导入smtplib和MIMEText
'''
http://smilejay.com/2013/03/python3-mysql-connector/
http://www.tuicool.com/articles/yqayEv
使用pymysql
'''

__author__ = 'tyler.yan'
#导入pymysql的包
import pymysql
try:
  #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
  conn=pymysql.connect(host='192.168.100.87',user='tearch_user',passwd='abc123',db='service_monitor',port=3306,charset='utf8')
  cur=conn.cursor()#获取一个游标
  cur.execute('select * from qm_log_count_stats')
  data=cur.fetchall()
  for d in data :
    #注意int类型需要使用str函数转义
    print("ID: "+str(d[0])+'  type： '+d[1]+"  service_name： "+d[2])
  
except  Exception as e :
  print("发生异常" +str(e))
finally:
  cur.close()#关闭游标
  conn.close()#释放数据库资源  
  
print("Good Bye!")  