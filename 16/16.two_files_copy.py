# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 02:55:28 2019

@author: prathulsai
"""
f=input()
t=input()
a=open(f,'r')
s=a.read()
b=open(t,'w')
b.write(s)
print("copied from ",f,"to ",t)
a.close()
b.close()
