# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:34:19 2022

@author: Sebastian
"""

lines = []
vowels = 0
consonants_count = 0
consonants = 'bcdfghjklmnpqrstvxwz'
print('How many lines will there be?')
linesNumber = int(input())
print('Enter your poem : ')
for i in range(linesNumber):
    a = input().lower()
    lines.append(a)
    for letter in a:
        if letter in 'aeiou':
            vowels = vowels + 1
        elif letter in consonants:
            consonants_count = consonants_count + 1

print('Number of lines ' + str(linesNumber))
print('Number of vowels ' + str(vowels))
print('Number of consonants ' + str(consonants_count))