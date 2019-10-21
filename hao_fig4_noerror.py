# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:55:40 2019

@author: azumi
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime

p0_list=[i for i in np.linspace(0,1,100)]
#w_list=[i for i in np.linspace(1,0.3,100)]
#kappa_list=[i for i in np.linspace(R,P,20)]

def cal(delta,chi,w,p0):# calculate phi
    kappa=P+delta
    
    phi_1=((1-w)*(1-p0))/((chi-1)*(R-kappa))
    phi_2=(1-(1-w)*p0)/((chi-1)*(R-kappa)+(chi*(T-R)+(R-S)))
    phi_3=(w+(1-w)*p0)/((chi-1)*(kappa-P)+(chi*(P-S)+(T-P)))
    phi_4=(1-w)*p0/((chi-1)*(kappa-P))
    return phi_1,phi_2,phi_3,phi_4

def cal2(w):# Check conditions of phi
    #chi_list=[i for i in np.linspace(1,21,100)]#100
    chi_list=[i for i in np.linspace(1.0001,21,100)]#100
    #delta_list=[i for i in np.linspace(0,1,1000)]#10000
    delta_list=[i for i in np.linspace(0+0.0001,1-0.0001,100)]#10000
    p0_list=[i for i in np.linspace(0,1,100)]#100
    delta_list2=[]
    chi_list2=[]
    p0_list2=[]
    
    for delta in delta_list:
        min_chi=100
        tmp_delta=100
        tmp_p0=100
        for p0 in p0_list:
            for chi in chi_list:
                phi_1,phi_2,phi_3,phi_4=cal(delta,chi,w,p0)
                
                if phi_1<=phi_2 and phi_1<=phi_3 and phi_4<=phi_2 and phi_4<=phi_3:                
                    if min_chi>chi:
                        min_chi=chi
                        tmp_delta=delta
                        tmp_p0=p0

        if tmp_p0==100 or min_chi==100 or tmp_delta==100:
            continue
        
        delta_list2.append(tmp_delta)
        chi_list2.append(min_chi)
        p0_list2.append(tmp_p0)
    #print(p0_list2)
    #print(delta_list2)
    #plt.plot(p0_list2)
    my_plot(chi_list2,delta_list2,w)

def my_plot(x,y,w):# generate the figure and setting of the figure
    plt.ylim(0,)
    plt.xlim(0,20)
    plt.xlabel('$\chi$')
    plt.ylabel('$\Delta$')
    plt.grid()
    plt.plot(x,y)
    
    plt.savefig('./figure/w_{}_noerror.png'.format(w))

if __name__ == "__main__":
    T,R,P,S=1.5,1,0,-0.5
    #T,R,P,S=5,3,1,0
    w_list=[0.4]
    dt_start = datetime.datetime.now()
    print("start time: {}".format(dt_start))
    print("----")
    
    for w in w_list:
        dt_now = datetime.datetime.now()
        print("time: {}".format(dt_now))
        print("Calculating in the case of w={}...".format(w))
        cal2(w)
    
    print("----")
    dt_end = datetime.datetime.now()
    print("ending time: {}".format(dt_end))
    print("Calculating time: {}".format(dt_end-dt_start))