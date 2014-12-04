#!/usr/bin/env python
#coding:utf-8

#python logging:https://docs.python.org/3.1/library/logging.html
import logging
#import time
import threading
from time import ctime,sleep

logging.basicConfig(filename='example.log',level=logging.DEBUG)
def music(func):
    for i in range(20):
        try:
            logging.info(str(i) + "I was at the %s! %s" %(func,ctime()))            
            sleep(1)
        except Exception as e:
            logging.error(str(e));
 
def move(func):
    for x in range(20):        
        try:
            logging.info(str(x) + "I was at the %s! %s %d" %(func,ctime(),x) )
            sleep(5)
        except Exception as e:
            logging.error(str(e))


    
threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)
     
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()     
    logging.info("all over %s" %ctime() )