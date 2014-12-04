#!/usr/bin/python
#encoding=utf-8
from pip._vendor.distlib.compat import raw_input
import sys;

#guide http://www.cnblogs.com/allenblogs/archive/2010/09/13/1824842.html

#exp = raw_input("\n\n Press the enter key to exit.")
#print(exp)
 
#name = input('What is your name?\n')
#print('Hi, %s.' % name)

#read file
fo = open("foo.txt",'r')
#fo = open("foo.txt")
print("Name of the file: %s" % fo.name);
print( "Closed or not : %s" % fo.closed);
print("Opening mode : %s" % fo.closed);


try:     
     lines = fo.readlines()      
     for line in lines:
          print(line)
finally:
     fo.close( )
     
wlines = ['ali','baidu','tencent','sina']     
#write file     
writeFile = open('data', 'w')     

try:
     writeFile.writelines(wlines)
finally:
     writeFile.close()

#read file by content size.     
file = open('test.log', 'r')
sizehint = 209715200   # 200M
position = 0
lines = file.readlines(sizehint)
while not file.tell() - position < 0: 
     position = file.tell()
     lines = file.readlines(sizehint)     
     print("lines")
else:
     print("this is the end!")












