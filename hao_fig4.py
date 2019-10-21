# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:55:40 2019

@author: azumi
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime
import csv
from argparse import ArgumentParser


#--parameter setting (default)--
default_settings={'delta':1000,# step size of delta ,0<=delta<=R-P
                  'chi':1000,# step size of chi ,0<=chi<=25
                  'eta':0.03}# error rate eta=epsilon+xi

payoff={'T':1.5, 'R':1.0, 'P':0.0, 'S':-0.5}

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--delta', metavar='delta_StepSize', type=float,
                        default=default_settings['delta'])
    parser.add_argument('--chi', metavar='chi_StepSize', type=float,
                        default=default_settings['chi'])
    parser.add_argument('--eta', metavar='error_rate_eta', type=float,
                        default=default_settings['eta'])
    args = parser.parse_args()
    return args

def cal_phi(eta,delta,chi):# calculate phi
    RE = R*(1-eta)+S*eta
    SE = S*(1-eta)+R*eta
    TE = T*(1-eta)+P*eta
    PE = P*(1-eta)+T*eta
    
    mu=1-eta
    
    phi_1=(chi-1)*(RE-PE-delta)-eta/(mu-eta)*((RE-SE)+chi*(TE-RE))
    phi_2=(chi-1)*(RE-PE-delta)+mu/(mu-eta)*((RE-SE)+chi*(TE-RE))
    phi_3=(chi-1)*delta+mu/(mu-eta)*((TE-PE)+chi*(PE-SE))
    phi_4=(chi-1)*delta-eta/(mu-eta)*((TE-PE)+chi*(PE-SE))
    
    return phi_1,phi_2,phi_3,phi_4

def cal(args):# Check conditions of phi
    chi_list=[i for i in np.linspace(1,25,args.chi)]#1000
    delta_list=[i for i in np.linspace(0,1,args.delta)]#1000
    delta_list2=[]
    chi_list2=[]
    eta=args.eta
    
    for delta in delta_list:
        min_chi=100
        tmp_delta=100
        for chi in chi_list:
            phi_1,phi_2,phi_3,phi_4=cal_phi(eta,delta,chi)
            if phi_1>=0 and phi_2>=0 and phi_3 >= 0 and phi_4>=0 and min_chi>chi:
                min_chi=chi
                tmp_delta=delta
        if min_chi==100 or tmp_delta==100:
            continue
        delta_list2.append(tmp_delta)
        chi_list2.append(min_chi)
        
    #my_plot(chi_list2,delta_list2,eta)# create the figure
    write_csv(chi_list2,delta_list2,args)

def write_csv(x,y,args):
    with open('./data/csv/nondiscount/eta_{}.csv'
              .format('{:.4f}'.format(args.eta).replace('.', '')), 'w') as f:
        
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows([x,y])
    
def my_plot(x,y,eta):# create the figure and setting
    plt.ylim(0,)
    plt.xlim(0,20)
    plt.xlabel('$\chi$')
    plt.ylabel('$\Delta$')
    plt.grid()
    plt.plot(x,y)
    
    plt.savefig('./data/figure/eta_{}_nondiscount.png'.format(eta))
    

if __name__ == "__main__":
    args = parse_args()# Parsing
    T,R,P,S=payoff['T'],payoff['R'],payoff['P'],payoff['S']
    
    dt_start = datetime.datetime.now()
    print("start time: {}".format(dt_start))
    print("----")
    
    dt_now = datetime.datetime.now()
    print("time: {}".format(dt_now))
    print("Calculating in the case of eta={:.4f} ...".format(args.eta))
    cal(args)
    
    print("----")
    dt_end = datetime.datetime.now()
    print("ending time: {}".format(dt_end))
    print("Calculating time: {}".format(dt_end-dt_start))
