# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 01:24:24 2019

@author: prathulsai
"""
class splits:
    def a(self):
        b=input()
        b=b.split()
        b.reverse()
        return " ".join(b)
d=splits()
print(d.a())