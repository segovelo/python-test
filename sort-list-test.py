# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:03:31 2022

@author: Sebastian
"""

list1 = [9,0,4,0,1,0,0,0,0,7,0,0,5]
length = len(list1)
c = 0
i = 0

while i < (length - 1):
    c = c + 1
    print('cycle : ' + str(c))

    if list1[i] == 0:
        j = i
        print(' initial i ' + str(i))
        print(' initial j ' + str(j))
        while i < (length - 1) and (list1[i] == 0):
            i = i + 1
            print(' i inside while loop : '+ str(i))
        print(' After while loop j  ' + str(j))
        temp = list1[j]
        print(' list1[i] : ' + str(list1[i]))
        print('temp : ' + str(temp))
       
        list1[j] = list1[i]
        list1[i] = temp
        print(list1)
        print('====================================')
    else:
        i = i + 1

print(list1)