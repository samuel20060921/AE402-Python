# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:29:34 2022

@author: gamin
"""

scores = [['chris', 83],['david', 96],['bill', 92],['amy', 59],['james', 77]] 
      
studentname = [scores[i][0] for i in range(len(scores))]
print(studentname)

studentscore = [scores[i][1] for i in range(len(scores))]
print(studentscore)

maxindex = studentscore.index(max(studentscore))
print(f'highest: {studentname[maxindex]}, {max(studentscore)}')

minindex = studentscore.index(min(studentscore))
print(f'lowest: {studentname[minindex]}, {min(studentscore)}')
