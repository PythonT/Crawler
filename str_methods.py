#!/usr/bin/python
#coding:utf-8
# Filename: str_methods.py

name = 'Swaroop' # 这是一个字符串对象

if name.startswith('Swa'):

    print('Yes, the string starts with "Swa"')

if 'a' in name:

    print('Yes, it contains the string "a"')

if name.find('war') != -1:

    print('Yes, it contains the string "war"')

delimiter = '_*_'

mylist = ['Brazil', 'Russia', 'India', 'China']

print(delimiter.join(mylist))