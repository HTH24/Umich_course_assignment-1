# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:54:58 2020

@author: 胡天行
"""


with open('test.txt') as text_file:
    tf = text_file.readlines() # tf is a list
    # print(tf)
    # print(type(tf))
    list = []
    # print(tf[25])
    for i in tf:
        # i = i.rstrip()
        y = re.findall('[0-9]+', i)
        # print(y)
        # if len(y) < 1: 
        #     continue

        for i in range(len(y)):
            num = float(y[i])
            list.append(num)
print(sum(list))