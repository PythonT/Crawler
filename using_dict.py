#!/usr/bin/python
#coding:utf-8
# Filename: using_dict.py

# 'ab'是'a'ddress'b'ook的缩写

ab = {  'Swaroop'   : 'swaroop@swaroopch.com',

        'Larry'     : 'larry@wall.org',

        'Matsumoto' : 'matz@ruby-lang.org',

        'Spammer'   : 'spammer@hotmail.com'

    }

print("Swaroop's address is", ab['Swaroop'])

#字典就像通讯录，只要知道联系人的名字就能找到他的地址或详细信息。即我们将键(名字)与值(相关信息)联系到一起。

#注意键必须是唯一的，这就像如果两个人同名你就没法找到正确的信息了。

#还有字典的键必须是不可变对象（比如字符串），但字典的值可以是可变或不可变对象。基本上这意味着只能将简单的对象作为键。

#字典中的键值对使用语法d = {key1 :value1, key2: value2}指定。

#其中键和值由分号分隔而所有的键值对用逗号分隔，并且它们被括在一对大括号内。

#记住字典中的键值对是无序的。如果你希望按照特定的顺序排列它们，你只能在使用前自己排序。

#而你实际使用的字典是dict类的对象/实例。