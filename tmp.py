# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 00:59:35 2019

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


    
def minimum_discount_w_c(eta,v):
    R,S,T,P=v[0],v[1],v[2],v[3]
    RE = R*(1-eta)+S*eta
    SE = S*(1-eta)+R*eta
    TE = T*(1-eta)+P*eta
    PE = P*(1-eta)+T*eta
    
    #RE,SE,TE,PE = R,S,T,P
    
    mu=1-eta
    
    w1=(TE-RE)/(mu*(TE-PE)+eta*(SE-RE))
    w2=(PE-SE)/(mu*(RE-SE)+eta*(PE-SE))
    
    return max(w1,w2)

def main():    
    T,R,P,S=1.5,1,0,-0.5
    #T,R,P,S=5,3,1,0
    
    payoff_vector=[R,S,T,P]
    
    list_w=[]
    list_error=[]
    
    for i in range(0,500):
        eta=i/1000
        
        if minimum_discount_w_c(eta,payoff_vector)>1:
            break
        w_c=minimum_discount_w_c(eta,payoff_vector)
        list_w.append(w_c)
        list_error.append(eta)
        print(eta,w_c)
    
    plt.plot(list_error,list_w,'o',markersize=1,color='#e8204e')
    plt.ylabel(r"$w_c$",fontsize=18)
    plt.xlabel(r"$\epsilon+\xi$",fontsize=18)
    plt.grid()
    plt.xlim(0,0.3)
    plt.ylim(0, 1)

if __name__ == "__main__":
    #relative_path='./data/csv/marged_w/'
    relative_path='./data/w_c/1000/'
    dir_list=os.listdir(relative_path)
    w=0
    for file in dir_list:
        w_before = w
        eta,w = return_xy(relative_path, file)
        #print((w-w_before))
        my_plot(eta,w)
    main()
    plt.savefig('./equalizer_wc_tmp.pdf')