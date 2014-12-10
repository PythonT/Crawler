#!/usr/bin/python
#coding:utf-8
# Filename: keyword_only.py

def total(initial=5, *numbers, vegetables):

    count = initial

    for number in numbers:

        count += number

    count += vegetables

    return count

print(total(10, 1, 2, 3, vegetables=50))

print(total(10, 1, 2, 3)) # 引发错误，因为我们没有为vegetables提供默认实参值