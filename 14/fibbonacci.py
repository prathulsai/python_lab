# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 03:14:15 2019

@author: prathulsai
"""
def fib(n):
    a=0
    b=1
    print("0 1",end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c