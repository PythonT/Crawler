#!/usr/bin/python
#coding:utf-8
# Filename: total.py

#当我们以星号声明一个形参比如*param，那么这个参数点之后的所有实参会被收集成一个列表，

#本例中这个列表叫做param。与之类似如果我们以双星号声明一个形参，它会被收集成一个关键字实参字典。
def total(initial=5, *numbers, **keywords):

    count = initial
    
    print(count)

    for number in numbers:

        print(number)
        count += number

    for key in keywords:
        print(key)
        count += keywords[key]

    return count

print(total(10, 1, 2, 3, vegetables=50, fruits=100))