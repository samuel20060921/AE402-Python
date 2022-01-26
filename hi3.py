# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:15:50 2022

@author: gamin
"""
import random
num = random.randint(1, 20)

i = 0
while i < 5:
    ans = input('give a number (1-20): ')
    ans = int(ans)
    i = i + 1
    if num == ans:
        print('correct')
        print(i)
    elif ans > num:
        print('too big')
    elif ans < num:
        print('too small')
if i >= 5:
    print('you failed')
        