#!/usr/bin/python
#coding:utf-8

# Filename: using_file.py 

poem = '''/

Programming is fun

When the work is done

if you wanna make your work also fun:

    use Python!

'''

 

f = open('poem.txt', 'w') # 写模式打开

f.write(poem) # 写文件

f.close() # 关闭文件

 

f = open('poem.txt') # 如果没有提供打开模式, 则默认假设为读模式

while True:

    line = f.readline()

    if len(line) == 0: # 长度为0代表EOF(注: end of file即文件尾)

        break

    print(line, end='')

f.close() # close the file