#!/usr/bin/python
#coding:utf-8

# Filename: using_tuple.py

zoo = ('python', 'elephant', 'penguin') # 注意小括号是可选的

print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)

print('Number of cages in the new zoo is', len(new_zoo))

print('All animals in new zoo are', new_zoo)

print('Animals brought from old zoo are', new_zoo[2])

print('Last animal brought from old zoo is', new_zoo[2][2])

print('Number of animals in the new zoo is',

len(new_zoo)-1+len(new_zoo[2]))

#元组用于保存各种各样的对象。它与列表很相似，但它缺少列表提供的大量功能。

#列表的一个主要特点就象字符串一样，它是不可变类型，也就是说你不可以修改元组。

#元组通过一组以逗号分隔的元素定义，并以一个可选的小括号闭合。

#元组通常用于这样的情形，一个语句或一个用户定义的函数能够安全的假设其使用的一组值(即元组值)不会发生改变。