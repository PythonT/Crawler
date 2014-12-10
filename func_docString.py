#!/usr/bin/python
#coding:utf-8
# Filename: func_doc.py

def printMax(x, y):

    '''Prints the maximum of two numbers.

    The two values must be integers.'''

    x = int(x) # convert to integers, if possible

    y = int(y)

    if x > y:

        print(x, 'is maximum')

    else:

        print(y, 'is maximum')

printMax(3, 5)

print(printMax.__doc__)

#一个函数的第一个逻辑行的字符串将成为这个函数的文档字符串。

#注意类和模块同样拥有文档字符串，在后面相应的章节我们会学到它们。

#根据惯例，文档字符串是一个多行字符串，其中第一行以大写字母开头，并以句号结尾。

#接下来的第二行为空行，从第三行开始为详细的描述。

#我强烈建议你在你的正规函数中遵循这个编写文档字符串的惯例。

#我们可以通过使用函数的__doc__属性(注意双下划线)存取printMax的文档字符串。

#记住python中的一切都是对象，其中也包括函数。在后面的类一章我们会学到更多。

#如果你在python使用过help()，其实你已经看到过文档字符串的应用了！

#help()只是取出函数的__doc__属性，然后以一种整洁的方式显示给你。

#你可以用上面的函数作个实验 – 在你的程序中包含help(printMax)即可，记住按q键退出help。