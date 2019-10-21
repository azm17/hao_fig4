# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:23:14 2019

@author: azumi
"""
import matplotlib.pyplot as plt
import csv
import os

def my_plot(x,y,filename):# generate the figure and setting of the figure
    plt.figure()
    plt.ylim(0,)
    plt.xlim(0,20)
    plt.xlabel('$\chi$')
    plt.ylabel('$\Delta$')
    plt.grid()
    plt.plot(x,y)
    
    plt.savefig('./data/figure/nodiscount/{}.png'.format(filename))

def read_csv(filename):
    data=[]
    with open(filename+'.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    x=[float(i) for i in data[0]]
    y=[float(i) for i in data[1]]
    return x,y

if __name__ == "__main__":
    
    filedir='./data/csv/nondiscount/'
    
    for filename in os.listdir(filedir):
        name=filename[0:-4]
        x,y=read_csv(filedir+name)
        my_plot(x,y,name)
    