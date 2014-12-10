#!/usr/bin/python
#coding:utf-8

# Filename: reference.py

print('Simple Assignment')

shoplist = ['apple', 'mango', 'carrot', 'banana']

mylist = shoplist # mylist只是指向相同对象的另一个名字

del shoplist[0] # 我购买了第一个水果，所以把它从清单中删除

print('shoplist is', shoplist)

print('mylist is', mylist)

# 注意列表shoplist和mylist打印了相同的内容，其中都不包括’apple’，因为它们指向的是相同的对象。

print('Copy by making a full slice')

mylist = shoplist[:] # 以全切片创造一个列表的完整拷贝

del mylist[0] # 删除第一个元素

print('shoplist is', shoplist)

print('mylist is', mylist)