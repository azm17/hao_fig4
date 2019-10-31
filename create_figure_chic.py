# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:19:28 2019

@author: azumi

make the figure of chi_c
cih >=1 strategies
"""
import matplotlib.pyplot as plt
import csv
import os

def my_plot(x,y,name):# generate the figure and setting of the figure
    
    plt.ylim(0,15)
    plt.xlim(0,0.3)
    plt.xlabel('$\eta=\epsilon+\\xi$')
    plt.ylabel('$\chi$')
    plt.grid()
    plt.plot(x,y,'o')
    #plt.savefig('../data/figure/nondiscount_hao/chic.png')
    #plt.savefig('../data/figure/nondiscount_hao/{}.png'.format(n))

def my_listplot(x_list,y_list,legend_list):
    plt.figure()
    plt.ylim(0,20)
    plt.xlim(0,0.3)
    plt.xlabel('$\eta=\epsilon+\\xi$')
    plt.ylabel('$\chi_c$')
    plt.grid()
    
    for x,y in zip(x_list,y_list):
        plt.plot(x,y,'o')
    plt.legend(legend_list)
    plt.show()
    #plt.savefig('../data/figure/chic.png')

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
    relative_path='./data/csv/marged_w/'
    dir_list=os.listdir(relative_path)
    dir_list.reverse()# reverse dir_list
    x_list,y_list,w_list=[],[],[]
    
    for tmp_dir in dir_list:
        w_list.append(round(float(tmp_dir[2:])*0.1,1))
    
    for filedir in dir_list:
        filedir =relative_path+filedir+'/'
        x,y=[],[]
        for filename in os.listdir(filedir):
            name=filename[0:-4]
            eta=round(float(name[4:7])*0.01,2)
            w=round(float(name[10:])*0.1,2)
            
            x.append(eta)
            y.append(read_csv(filedir+name))
        
        x_list.append(x)
        y_list.append(y)
        
        #my_plot(x,y,name)
    
    my_listplot(x_list,y_list,w_list)

