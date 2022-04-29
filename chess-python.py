# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:53:57 2022

@author: Sebastian
"""

coordinates = [[1,1,2,2], [1,1,8,2], [2,3,2,8], [4,6,6,4]]

for i in range(len(coordinates)):
    if coordinates[i][0] == coordinates[i][2]:
        print('YES')
    elif coordinates[i][1] == coordinates[i][3]:
        print('YES')
    elif abs(coordinates[i][0] - coordinates[i][2]) == abs(coordinates[i][1] - coordinates[i][3]):
         print('YES')
    else:  
        print('NO')
    