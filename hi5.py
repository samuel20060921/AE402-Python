# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 10:20:13 2022

@author: gamin
"""

names = []
scores = []
total = 0
avg = 0
n = int(input('number of students:'))

for i in range(n):
    name = input('enter name: ')
    names.append(name)
    score = input('enter score: ')
    score = int(score)
    scores.append(score)

for item in scores:
    total = int(total) + int(item)
print ('avg:', (total/n))

highest = 0
for i in range(n):
    if scores[i] > highest:
        highest = scores[i]
        highestname = names[i]
print(highestname, 'has the highest score:', highest)

lowest = 100
for i in range(n):
    if scores[i] < lowest:
        lowest = scores[i]
        lowestname = names[i]
print(lowestname, 'has the lowest score:', lowest)
        
