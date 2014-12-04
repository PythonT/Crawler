#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib.request
from queue import Queue
import time,re,threading

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
lock = threading.Lock()# lock to serialize console output

def do_work(item):
    time.sleep(.1) # pretend to do some lengthy work.
    # Make sure the whole print completes or threads can mix up output in one line.
    with lock:
        print(threading.current_thread().name,item)
        try:
            image=item   
            link = (image.split('"'))[1].split('alt')[0]#get pic link                                                
            name = str(image.split(' ')[2]).split('"')[1]#get pic link  
            imgType = link.split('.')[-1]
            print(str(imgType) + ':' +name +":"+ str(link))
            try:                                    
                with urllib.request.urlopen(link,None,timeout=10) as url :                                                                                                                                                              
                    write_file(url.read(), './pic3/%s.%s'%(name,imgType))
            except Exception as e:print(e)                    
        except Exception as e:print(e)                 

def write_file(content,filePath):                                                
    fil = open(filePath,'wb')                                          
    fil.write(content)                         
    fil.close()           
    
# The worker thread pulls an item from the queue and processes it
def worker():
    while True:
        item = q.get()
        print('queue get ' + str(item))
        do_work(item)
        q.task_done()

def touchImages():
    url='http://www.qiushibaike.com/imgrank'
    req=urllib.request.Request(url,headers=head)
    res=urllib.request.urlopen(req)
    html=res.read().decode('utf8')    
    #rule=re.compile('<img src="(.\\?)" alt="(.\\?)" />')
    rule = re.compile('<img[^>]*>')
    return rule.findall(html) 

# Create the queue and thread pool.
q = Queue()
for i in range(4):
    t = threading.Thread(target=worker)
    t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
    t.start()
     
     
     
# stuff work items on the queue (in this case, just a number).
start = time.perf_counter()
images = [] + touchImages()
for item in images:    
    q.put(item)

q.join()# block until all tasks are done

# "Work" took .1 seconds per task.
# 20 tasks serially would be 2 seconds.
# With 4 threads should be about .5 seconds (contrived because non-CPU intensive "work")
print('time:',time.perf_counter() - start)    



 
