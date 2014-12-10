#!/usr/bin/python
#coding:utf-8

# Filename: pickling.py

import pickle

# the name of the file where we will store the object

shoplistfile = 'shoplist.data'

# the list of things to buy

shoplist = ['apple', 'mango', 'carrot']

 

# Write to the file

f = open(shoplistfile, 'wb')

pickle.dump(shoplist, f) # 转储对象到文件

f.close()

del shoplist # 销毁shoplist变量
 

# 从文件找回对象

f = open(shoplistfile, 'rb')

storedlist = pickle.load(f) # 从文件加载对象

print(storedlist)


#为了将对象存储到文件，我们必须首先’wb’写二进制文件模式打开文件然后调用pickle模块的dump函数。这个过程叫做封藏(pickling)对象。

#接下来我们使用pickle的load函数重新找回对象。这个过程叫做解封(unpickling)对象。