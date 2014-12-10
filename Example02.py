#!/usr/bin/env python
#coding:utf-8
#link:http://www.cnblogs.com/txw1958/archive/2012/12/10/2810973.html
age = 25
name = 'Swaroop'
print('{0} is {1} years old'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('{0:.3}'.format(1/3))
print('{0:_^11}'.format('hello')) #以下划线填充字符串到11位长, hello中间对齐
print( '{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python') )

length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))
