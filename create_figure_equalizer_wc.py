# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:00:43 2019

@author: Azumi Mamiya
"""
import matplotlib.pyplot as plt
import csv
import os

def my_plot(eta, w):# generate the figure and setting of the figure
    
    plt.ylim(0,1)
    plt.xlim(0,0.334)
    plt.xlabel('$\eta=\epsilon+\\xi$',fontsize=18)
    plt.ylabel('$w$',fontsize=18)
    plt.grid()
    plt.plot(eta,w,'o',color='#1f77b4',markersize=1)
    #plt.savefig('../data/figure/nondiscount_hao/{}.png'.format(n))

def return_xy(path, filename):
    
    eta = float(filename[4:8])*0.001
    with open(path+filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            w = float(row[0])    
    return eta, w

if __name__ == "__main__":
    #relative_path='./data/csv/marged_w/'
    relative_path='./data/w_c/1000/'
    dir_list=os.listdir(relative_path)[:214]
    print(dir_list)
    w=0
    for file in dir_list:
        w_before = w
        eta,w = return_xy(relative_path, file)
        #print((w-w_before))
        my_plot(eta,w)
    plt.grid()
    plt.savefig('./equalizer_wc.pdf')