# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:42:05 2022

@author: gamin
"""
math = input('enter math score')
english = input('enter english score')

mscore = int(math)
escore = int(english)

if mscore == 100 or escore == 100:
    print('congratulation, you got scholarship')
elif mscore >= 90 and escore >= 90:
    print('congratulation, you got scholarship')
else:
    print('sorry, no scholarship')

