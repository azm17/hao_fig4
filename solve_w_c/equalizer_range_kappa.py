# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:16:55 2020

@author: Azumi Mamiya
"""

import matplotlib.pyplot as plt
import numpy as np

payoff={'T':1.5, 'R':1.0, 'P':0.0, 'S':-0.5}
T,R,P,S=payoff['T'],payoff['R'],payoff['P'],payoff['S']

def my_plot(eta, w):# generate the figure and setting of the figure
    plt.ylim(0, 1)
    plt.xlim(0,0.211)
    plt.xlabel('$\epsilon+\\xi$',
               fontsize = 18)
    plt.ylabel('$s_Y$',
               fontsize = 18)
    
    plt.rcParams["xtick.direction"] = "in"  
    plt.rcParams["ytick.direction"] = "in"  
    plt.plot(eta, w, '-', 
             color = '#1f77b4', 
             markersize = 1)
    #plt.savefig('../data/figure/nondiscount_hao/{}.png'.format(n))

def func1(eta):
    mu = 1 - eta
    
    SE = S * mu + R * eta
    PE = P * mu + T * eta
    
    return (mu * PE - eta * SE) / (mu - eta)

def func2(eta):
    mu = 1 - eta
    
    RE = R * mu + S * eta
    TE = T * mu + P * eta    
    
    return (mu * RE - eta * TE)/ (mu - eta)

if __name__ == "__main__":
    eta_list = [i for i in np.linspace(0, 0.211, 100)]
    kappa_list1 = []
    kappa_list2 = []
    
    print(0,func1(0),func2(0))
    print(0.1,func1(0.1),func2(0.1))
    print(0.2,func1(0.2),func2(0.2))
    
    for eta in eta_list:
        kappa_list1.append(func1(eta))
        kappa_list2.append(func2(eta))
        
        
    my_plot(eta_list, kappa_list1)
    my_plot(eta_list, kappa_list2)
    plt.grid()
    plt.savefig('./equa_kappa_range.pdf')