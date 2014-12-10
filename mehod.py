#!/usr/bin/python
#coding:utf-8

#Filename:method.py

class Person:
    
    #__init__方法在类对象被实例化时立即执行。此方法专用于初始化对象。另外注意方法名中的双下划线前后缀。
    def __init__(self,name):
        self.name = name
        
    def sayHi(self):
        print('hello world,',self.name)
        
p = Person('tyler')

p.sayHi()

#Person('tyler').sayHi()

#本利中我们使用了self，注意方法sayHi虽无需参数但在函数中仍然要写上self。