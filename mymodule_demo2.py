#!/usr/bin/python
#coding:utf-8

# Filename: mymodule_demo2.py

from mymodule import sayhi, __version__
#from mymodule import * 

sayhi()

print('Version', __version__)

#注意我们同样使用点号访问模块成员。

#python很好的重复利用了相同的符号，带来独特的’Pythonic’感受，这样我们就不必学习更多的语法知识了。