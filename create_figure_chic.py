# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:19:28 2019

@author: azumi
"""
import matplotlib.pyplot as plt
import csv
import os

def my_plot(x,y,filename):# generate the figure and setting of the figure
    plt.figure()
    plt.ylim(0,15)
    plt.xlim(0,0.3)
    plt.xlabel('$\eta=\epsilon+\\xi$')
    plt.ylabel('$\chi$')
    plt.grid()
    plt.plot(x,y,'o')
    plt.savefig('../data/figure/nondiscount_hao/chic.png')
    #plt.savefig('../data/figure/nondiscount_hao/{}.png'.format(n))

def read_csv(filename):
    data=[]
    with open(filename+'.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    x=[float(i) for i in data[0]]
    #y=[float(i) for i in data[1]]
    if x==[]:
        pass
    else:
        return min(x)

if __name__ == "__main__":
    
    filedir='../data/csv/nondiscount_hao/'
    x,y=[],[]
    for filename in os.listdir(filedir):
        name=filename[0:-4]
        x.append(round(float(name[4:])*0.0001,5))
        y.append(read_csv(filedir+name))
    
    my_plot(x,y,name)