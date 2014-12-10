#!/usr/bin/python
#coding:utf-8

def reverse(text):
    text = text.lower()
    text = text.replace(",", "");
    text = text.replace(".", "");
    text = text.replace(" ", "");
    print(text)
    return text[::-1]

def is_palindrome(text):
    
    return text == reverse(text)

something = input('enter text:')

if(is_palindrome(something)):
    print('yes!')
else:
    print('no')

