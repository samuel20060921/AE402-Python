# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:50:39 2022

@author: gamin
"""

data = {'a01':['gummy bears', 20], 
        'a02':['popsicle', 25], 
        'a04':['noodles', 10], 
        'a06':['soda', 30]}

while True:
    ans = int(input('1.check items\n2.exit\nenter number: '))
    if ans == 1:
        num = input('enter item number: ')

        if num not in data:
            print('item {} does not exist'.format(num))
            new = input('add new item?(Y or N): ')
            if new == 'Y':
                name = input('enter item: ')
                money = int(input('enter item price: '))
                data[num] = [name, money]
                d = data.get(num)
                print(d)
                print('item number: {} item: {} price: {} dollars'.format(num, d[0], d[1]))
        else:
            print('item: {} price: {} dollars'.format(data[num][0], data[num][1]))
    elif ans == 2:
        break
    else:
        print('error, please re-enter')
        