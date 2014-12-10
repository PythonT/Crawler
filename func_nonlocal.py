#!/usr/bin/python
#coding:utf-8
# Filename: func_nonlocal.py

def func_outer():

    x = 2 # A 此处X 既不是global 也不是local！

    print('x is', x)

    def func_inner():

        nonlocal x #使用nonlocal改变A处 X的值
        #global x #请注意nonlocal  和golobal的区别

        x = 5

    func_inner()

    print('Changed local x to', x)

func_outer()