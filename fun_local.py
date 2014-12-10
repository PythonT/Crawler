#!/usr/bin/python
#coding:utf-8
# Filename: func_local.py

x = 50

def func(x):

    print('x is', x)

    x = 2

    print('Changed local x to', x)

func(x)

print('x is still', x)