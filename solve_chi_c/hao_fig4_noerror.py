# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:55:40 2019

@author: azumi
"""

import numpy as np
#import matplotlib.pyplot as plt
import datetime
from argparse import ArgumentParser
import csv




# --parameter setting (default)--
default_settings={'p0':1000,# step size of p0 ,0<=p0<=1
                  'delta':1000,# step size of delta ,0<=delta<=R-P
                  'chi':1000,# step size of chi ,0<=chi<=25
                  'w':0.9}# discount factor, must satisfy the condition 0<w<1


payoff={'T':1.5, 'R':1.0, 'P':0.0, 'S':-0.5}

# --- ---
def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--p0', metavar='p0_StepSize',
                        type=float, 
                        default=default_settings['p0'])
    
    parser.add_argument('--delta', metavar='delta_StepSize',
                        type=float,
                        default=default_settings['delta'])
    
    parser.add_argument('--chi', metavar='chi_StepSize',
                        type=float,
                        default=default_settings['chi'])
    
    parser.add_argument('--w', metavar='discount_rate',
                        type=float,
                        default=default_settings['w'])
    
    
    args = parser.parse_args()
    return args

def cal(delta,chi,w,p0):# calculate phi
    kappa=P+delta
    
    phi_1=((1-w)*(1-p0))/((chi-1)*(R-kappa))
    phi_2=(1-(1-w)*p0)/((chi-1)*(R-kappa)+(chi*(T-R)+(R-S)))
    phi_3=(w+(1-w)*p0)/((chi-1)*(kappa-P)+(chi*(P-S)+(T-P)))
    phi_4=(1-w)*p0/((chi-1)*(kappa-P))
    return phi_1,phi_2,phi_3,phi_4

def cal2(args):# Check conditions of phi
    chi_list=[i for i in np.linspace(1.0001,21,args.chi)]#1000
    delta_list=[i for i in np.linspace(0+0.0001,1-0.0001,args.delta)]#1000
    p0_list=[i for i in np.linspace(0,1,args.p0)]#1000
    delta_list2,chi_list2,p0_list2=[],[],[]
    
    for delta in delta_list:
        progress=round(delta/delta_list[-1]*100)# for checking progress rate(%)
        if int(progress)%20==0:
            print('{}%'.format(int(progress)))
        min_chi=100
        tmp_delta=100
        tmp_p0=100
        for p0 in p0_list:
            for chi in chi_list:
                phi_1,phi_2,phi_3,phi_4=cal(delta,chi,args.w,p0)
                
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
    
    #my_plot(chi_list2,delta_list2,w)
    #write_csv(chi_list2,delta_list2,args)# output data

# output csv data 
def write_csv(x,y,args):
    with open('./data/csv/discount1101/eta_{}_w_{}.csv'
              .format('{:.2f}'.format(0).replace('.', ''),
              '{:.1f}'.format(args.w).replace('.', '')), 'w') as f:
        
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows([x,y])
"""
def my_plot(x,y,w):# generate the figure and setting of the figure
    plt.ylim(0,)
    plt.xlim(0,20)
    plt.xlabel('$\chi$')
    plt.ylabel('$\Delta$')
    plt.grid()
    plt.plot(x,y)
    
    plt.savefig('./figure/w_{}_noerror.png'.format(w))
"""

if __name__ == "__main__":
    args = parse_args()# Parsing
    T,R,P,S=payoff['T'],payoff['R'],payoff['P'],payoff['S']
    dt_start = datetime.datetime.now()
    print("start time: {}".format(dt_start))
    print("----")
    
    dt_now = datetime.datetime.now()
    print("time: {}".format(dt_now))
    print("Calculating in the case of w={}...".format(args.w))
    cal2(args)
    
    print("----")
    dt_end = datetime.datetime.now()
    print("ending time: {}".format(dt_end))
    print("Calculating time: {}".format(dt_end-dt_start))