# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:03:31 2022

@author: Sebastian
"""

list1 = [4,0,1,0,0,6,0,7,0,0,0]
length = len(list1)
c = 0
for i in range(length - 1):
    if list1[i] == 0:
        j = i
        i = i + 1
        while i < length - 1 and list1[i] == 0:
            i = i + 1
        temp = list1[j]
        list1[j] = list1[i]
        list1[i] = temp
    c = c + 1
    print(c)

print(list1)