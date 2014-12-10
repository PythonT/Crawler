#!/usr/bin/python
#coding:utf-8
# Filename: using_name.py

if __name__ == '__main__':

    print('This program is being run by itself')

else:

    print('I am being imported from another module')
    
#每个python模块都有自己的__name__定义，如果它是’__main__’则暗示模块为独立运行，我们可以进行一些适当的处理。