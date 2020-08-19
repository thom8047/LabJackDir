# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:25:50 2020

@author: Kyle
"""

import pandas
import matplotlib.pyplot as plt
import matplotlib.figure as fig

data = pandas.read_csv('Data')

valueHolder = {'Ad spend': 'Dollar Amount',
               'Sessions': 'Number of visits to page',
               'Conversion rate': 'Percentage of visits to page that purchase',
               'Sales less distributors': 'Dollar Amount',
               'credit cards as a % of orders': 'Percentage of CreditCard Orders',
               'Hours spend on R&D': 'Hours',
               'Visits to compliance page': 'Int',
               'Hours spend on Sales/Biz Dev': 'Hours'
               }

"""                           # FOR LOOP TO GET DATA WITH RESPECTIVE TYPE
for c in data.columns:
    print(c, end='\n')
    for d in data[c]:
        print(type(d), d)
"""
text = f'From the dates of {data["Week"][0]} to {data["Week"][22]} we have the following sums and means:\n'

for column in data.columns:
    if data[column].dtype != 'object':
        if column != 'Index':
            text += f'\nFor Column Name: {column:^30} | Sum: {data[column].sum():^20} | Mean: {data[column].mean():^20}'
            
            who = plt.figure(figsize=(12, 5))#, tight_layout=True)
            fig.Figure.subplots_adjust(who, wspace=0.5)
            fig.Figure.text(who, x = 0.5, y = 0.025, s=valueHolder[column])
            
            plt.subplot(131)
            plt.bar(data[column], data['Week'])
            plt.subplot(132)
            plt.scatter(data[column], data['Week'])
            plt.subplot(133)
            plt.plot(data[column], data['Week'])
            
            plt.suptitle(f'Graphs For Column: {column}\nY-Axis Represents Dates, X-Axis Represents {valueHolder[column]}')
        
        title = 'Graphs_For_Column({})'.format(column.replace('/', '')) + '.pdf'
        plt.savefig(title, bbox_inches='tight')

text_file = open('Data_Text', 'w')
text_file.write(text)
text_file.close()



