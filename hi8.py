# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:29:58 2022

@author: gamin
"""

print('-'*18)
print('Python Apple Store')
print('-'*18)

num = 0
sale = 0
sales = []

while True:
    print('functions=>')
    print('1. settings')
    print('2. import')
    print('3. export')
    print('4. total revenue')
    print('5. stock numbers')
    print('6. exit')
    
    sel = input('enter function: ')
    if sel == '1':
        num = int(input('enter apple amount: '))
        price = int(input('enter apple price: '))
        print('there are currently', num, 'apples')
        print('each apple is', price, 'dollars')
    
    elif sel == '2':
        numim = int(input('enter import amount: '))
        num = num + numim
        print('there are currently', num, 'apples')
    
    elif sel == '3':
        numex = int(input('enter export amount: '))
        print('please pay', numex*price, 'dollars')
        num = num - numex
        sale = sale + numex
        sales.append(numex)
        print('there are currently', num, 'apples')
    
    elif sel == '4':
        for i in range(len(sales)):
            print(sales[i], 'apples', sales[i]*price, 'dollars')
        total = sale*price
        print('total sale:', sale, 'apples')
        print('total revenue:', total, 'dollars')
    
    elif sel == '5':
        print('there are currently', num, 'apples')
    
    elif sel == '6':
        break
    
    else:
        print('wrong input, enter number')