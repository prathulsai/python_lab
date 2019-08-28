# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 02:34:11 2019

@author: prathulsai
"""
c=open("sai.txt",'r')
a=c.read()
a=a.split()
a=list(set(a))
a.sort()
print ("\n".join(a))
