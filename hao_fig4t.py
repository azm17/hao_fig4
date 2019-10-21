# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:55:40 2019

@author: azumi
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime


#p0_list=[i for i in np.linspace(0,1,100)]
#w_list=[i for i in np.linspace(1,0.3,100)]
#kappa_list=[i for i in np.linspace(R,P,20)]


def cal_phi(epsilon,xi,delta,chi):# calculate phi
    RE = R*(1-epsilon-xi)+S*(epsilon+xi)
    SE = S*(1-epsilon-xi)+R*(epsilon+xi)
    TE = T*(1-epsilon-xi)+P*(epsilon+xi)
    PE = P*(1-epsilon-xi)+T*(epsilon+xi)
    
    eta=epsilon+xi
    mu=1-epsilon-xi
    
    phi_1=(chi-1)*(RE-PE-delta)-eta/(mu-eta)*((RE-SE)+chi*(TE-RE))
    phi_2=(chi-1)*(RE-PE-delta)+mu/(mu-eta)*((RE-SE)+chi*(TE-RE))
    phi_3=(chi-1)*delta+mu/(mu-eta)*((TE-PE)+chi*(PE-SE))
    phi_4=(chi-1)*delta-eta/(mu-eta)*((TE-PE)+chi*(PE-SE))
    
    return phi_1,phi_2,phi_3,phi_4

def cal(epsilon,xi):# Check conditions of phi
    chi_list=[i for i in np.linspace(1,22,1000)]#1000
    delta_list=[i for i in np.linspace(0,1,1000)]#1000
    delta_list2=[]
    chi_list2=[]
    for delta in delta_list:
        min_chi=100
        tmp_delta=100
        for chi in chi_list:
            phi_1,phi_2,phi_3,phi_4=cal_phi(epsilon,xi,delta,chi)
            if phi_1>=0 and phi_2>=0 and phi_3 >= 0 and phi_4>=0 and min_chi>chi:
                min_chi=chi
                tmp_delta=delta
        if min_chi==100 or tmp_delta==100:
            continue
        delta_list2.append(tmp_delta)
        chi_list2.append(min_chi)
        
    eta=epsilon+xi
    my_plot(chi_list2,delta_list2,eta)# create the figure


def my_plot(x,y,eta):# create the figure and setting
    plt.ylim(0,)
    plt.xlim(0,20)
    plt.xlabel('$\chi$')
    plt.ylabel('$\Delta$')
    plt.grid()
    plt.plot(x,y)
    
    plt.savefig('./figure/eta_{}_nodiscount.png'.format(eta))
    

if __name__ == "__main__":
    T,R,P,S=1.5,1,0,-0.5
    #for i in [0.03,0.05,0.07,0.09,0.15]:
    dt_start = datetime.datetime.now()
    print("start time: {}".format(dt_start))
    print("----")
    eta_list=[0.03*2,0.05*2,0.07*2]
    eta_list=[0.03*2]
    for eta in eta_list:
        dt_now = datetime.datetime.now()
        print("time: {}".format(dt_now))
        print("Calculating in the case of eta={} ...".format(eta))
        i=eta/2
        cal(i,i)
    
    print("----")
    dt_end = datetime.datetime.now()
    print("ending time: {}".format(dt_end))
    print("Calculating time: {}".format(dt_end-dt_start))
