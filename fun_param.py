#!/usr/bin/python
#coding:utf-8
# Filename: func_param.py

def printMax(a, b):

    if a > b:

        print(a, 'is maximum')

    elif a == b:

        print(a, 'is equal to', b)

    else:

        print(b, 'is maximum')

printMax(3, 4) # 直接提供字面值

x = 5

y = 7

printMax(x, y) # 以变量作为实参