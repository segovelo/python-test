# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:03:31 2022

@author: Sebastian
"""

list1 = [9,0,0,4,0,1,0,0,0,7,3,5]
length = len(list1)
i = 0
j = 0
print(list1)
while i < (length - 1):

    if list1[i] == 0:
        i = i + 1
        while i < (length - 1) and (list1[i] == 0):
            print(' Inside nested while loop : ' + str(i))
            i = i + 1

        temp = list1[j]       
        list1[j] = list1[i]
        list1[i] = temp
        j = j + 1
        
    else:
        print(' Inside nested while loop : ' + str(i))
        i = i + 1
        j = j + 1

print(list1)