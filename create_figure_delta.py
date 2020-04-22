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

def my_plot(x, y, name):# generate the figure and setting of the figure
    
    plt.ylim(0,15)
    plt.xlim(0,0.3)
    plt.xlabel('$\eta=\epsilon+\\xi$')
    plt.ylabel('$\Delta$')
    plt.grid()
    plt.plot(x,y,'o')
    #plt.savefig('../data/figure/nondiscount_hao/chic.png')
    #plt.savefig('../data/figure/nondiscount_hao/{}.png'.format(n))

def my_listplot(x_list, y_list, legend_list):
    plt.figure()
    plt.ylim(0, 1)
    plt.xlim(0, 0.3)
    plt.xlabel('$\epsilon+\\xi$', fontsize=18)
    plt.ylabel('$\Delta$', fontsize=18)
    plt.grid()
    
    for x,y in zip(x_list, y_list):
        plt.plot(x, y, '-')
    plt.legend(legend_list, title = '$w$')
    #plt.show()
    #plt.savefig('../data/figure/chic.png')
    plt.savefig('./chic.pdf')
    
def read_chicnoerrorcsv():
    data = []
    with open('./data/chi_c/figure_chi_c/chi_c_noerror.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    chic = [float(i) for i in data[1]]# convert string to float
    w = [float(i) for i in data[0]]
    
    
    return dict(zip(w, chic))

def read_csv(filename):
    data = []
    with open(filename+'.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    x = [float(i) for i in data[0]]
    y = [float(i) for i in data[1]]
    #y=[float(i) for i in data[1]]
    if x == []:
        pass
    else:
        return y[x.index(min(x))]

if __name__ == "__main__":
    #relative_path='./data/csv/marged_w/'
    relative_path='./data/chi_c/figure_chi_c/'
    dir_list = os.listdir(relative_path)
    dir_list.reverse()# reverse dir_list
    x_list,y_list,w_list=[],[],[]
    dir_list.pop(-1)# pop chi_c_noerror.csv
    
    chic_noerror=read_chicnoerrorcsv()
    
    for tmp_dir in dir_list:
        w_list.append(round(float(tmp_dir[1:])*0.1,1))
    print(w_list)
    
    for filedir in dir_list:
        filedir =relative_path+filedir+'/'
        x,y=[],[]
        for filename in os.listdir(filedir):
            name = filename[0:-4]
            #print(name[4:8])
            eta = round(float(name[4:8])*0.001,3)
            w = round(float(filedir[-3:-1])*0.1,1)
            x.append(eta)
            y.append(read_csv(filedir+name))
        
        x.insert(0,0)
        y.insert(0,chic_noerror[w])
        
        x_list.append(x)
        y_list.append(y)
        
        #my_plot(x,y,name)
    
    my_listplot(x_list,y_list,w_list)

