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


def cal(epsilon,xi,delta,chi,w,p0):# calculate phi
    RE = R*(1-epsilon-xi)+S*(epsilon+xi)
    SE = S*(1-epsilon-xi)+R*(epsilon+xi)
    TE = T*(1-epsilon-xi)+P*(epsilon+xi)
    PE = P*(1-epsilon-xi)+T*(epsilon+xi)
    
    eta=epsilon+xi
    mu=1-epsilon-xi
    
    phi_1=(1-(1-w)*p0)/((chi-1)*(RE-PE-delta)-eta/(mu-eta)*((RE-SE)+chi*(TE-RE)))
    phi_2=(1-(1-w)*p0)/((chi-1)*(RE-PE-delta)+mu/(mu-eta)*((RE-SE)+chi*(TE-RE)))
    phi_3=(w+(1-w)*p0)/((chi-1)*delta+mu/(mu-eta)*((TE-PE)+chi*(PE-SE)))
    phi_4=(w+(1-w)*p0)/((chi-1)*delta-eta/(mu-eta)*((TE-PE)+chi*(PE-SE)))
    
    phi_5=(1-p0)*(1-w)/((chi-1)*(RE-PE-delta)-eta/(mu-eta)*((RE-SE)+chi*(TE-RE)))
    phi_6=(1-p0)*(1-w)/((chi-1)*(RE-PE-delta)+mu/(mu-eta)*((RE-SE)+chi*(TE-RE)))
    phi_7=(1-w)*p0/((chi-1)*delta+mu/(mu-eta)*((TE-PE)+chi*(PE-SE)))
    phi_8=(1-w)*p0/((chi-1)*delta-eta/(mu-eta)*((TE-PE)+chi*(PE-SE)))
    
    return phi_1,phi_2,phi_3,phi_4,phi_5,phi_6,phi_7,phi_8

def cal2(epsilon,xi,w):# Check conditions of phi
    #chi_list=[i for i in np.linspace(1,21,100)]#100
    chi_list=[i for i in np.linspace(1,21,1000)]#1000
    #delta_list=[i for i in np.linspace(0,1,1000)]#10000
    delta_list=[i for i in np.linspace(0,1,1000)]#1000
    p0_list=[i for i in np.linspace(0,1,1000)]#1000 100*100*100　4min
    #p0_list=[0.5]
    delta_list2=[]
    chi_list2=[]
    p0_list2=[]
    
    for delta in delta_list:
        min_chi=100
        tmp_delta=100
        tmp_p0=100
        for p0 in p0_list:
            for chi in chi_list:
                phi_1,phi_2,phi_3,phi_4,phi_5,phi_6,phi_7,phi_8=cal(epsilon,xi,delta,chi,w,p0)
                
                if phi_1>=phi_5 and phi_1>=phi_6 and phi_1>=phi_7 and phi_1>=phi_8:
                    if phi_2>=phi_5 and phi_2>=phi_6 and phi_2>=phi_7 and phi_2>=phi_8:
                        if phi_3>=phi_5 and phi_3>=phi_6 and phi_3>=phi_7 and phi_3>=phi_8:
                            if phi_4>=phi_5 and phi_4>=phi_6 and phi_4>=phi_7 and phi_4>=phi_8:
                                if min_chi>chi:
                                    min_chi=chi
                                    tmp_delta=delta
                                    tmp_p0=p0
        
        if tmp_p0==100 or min_chi==100 or tmp_delta==100:
            continue
        
        delta_list2.append(tmp_delta)
        chi_list2.append(min_chi)
        p0_list2.append(tmp_p0)
    
    eta=epsilon+xi
    my_plot(chi_list2,delta_list2,eta,w)

def my_plot(x,y,eta,w):# generate the figure and setting of the figure
    plt.figure()
    plt.ylim(0,)
    plt.xlim(0,20)
    plt.xlabel('$\chi$')
    plt.ylabel('$\Delta$')
    plt.grid()
    plt.plot(x,y)
    
    plt.savefig('./figure/2/eta_{}_w_{}_noerror.png'.format(eta,w))

if __name__ == "__main__":
    T,R,P,S=1.5,1,0,-0.5
    dt_start = datetime.datetime.now()
    print("start time: {}".format(dt_start))
    print("----")
    eta_list=[0.03*2,0.05*2,0.07*2]
    #eta_list=[0.07*2]
    w_list=[0.95,0.9,0.85,0.8,0.75,0.7]
    
    for w in w_list:
        for eta in eta_list:
            dt_now = datetime.datetime.now()
            print("time: {}".format(dt_now))
            print("Calculating in the case of (eta,w)=({},{}) ...".format(eta,w))
            i=eta/2
            cal2(i,i,w)
    
    print("----")
    dt_end = datetime.datetime.now()
    print("ending time: {}".format(dt_end))
    print("Calculating time: {}".format(dt_end-dt_start))
