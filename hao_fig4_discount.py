# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:55:40 2019

@author: azumi

details: extended fig4 of hao et al PRE(2015) to discounted
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime
from argparse import ArgumentParser


#--parameter setting (default)--
default_settings={'p0':100,# step size of p0 ,0<=p0<=1
                  'delta':100,# step size of delta ,0<=delta<=R-P
                  'chi':100,# step size of chi ,0<=chi<=25
                  'w':0.8,# discount factor, must satisfy the condition 0<w<1
                  'eta':0.10}# error rate eta=epsilon+xi

payoff={'T':1.5, 'R':1.0, 'P':0.0, 'S':-0.5}
#---

"""
core i9-9900K (8 core 16 thread)
RAM32.0GB Windows 10 Pro

(delta,chi,p0)=(100,100,100)       13 seconds
(delta,chi,p0)=(100,1000,100)     120 seconds
(delta,chi,p0)=(1000,10000,100)  1046 seconds
(delta,chi,p0)=(1000,10000,1000)    3 hours?
"""

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--p0', metavar='p0_StepSize', type=float, 
                        default=default_settings['p0'])
    parser.add_argument('--delta', metavar='delta_StepSize', type=float,
                        default=default_settings['delta'])
    parser.add_argument('--chi', metavar='chi_StepSize', type=float,
                        default=default_settings['chi'])
    parser.add_argument('--w', metavar='discount_rate', type=float,
                        default=default_settings['w'])
    parser.add_argument('--eta', metavar='error_rate_eta', type=float,
                        default=default_settings['eta'])
    
    args = parser.parse_args()
    return args

def cal(eta,delta,chi,w,p0):# calculate phi
    # expected payoff against actions
    RE = R*(1-eta)+S*eta
    SE = S*(1-eta)+R*eta
    TE = T*(1-eta)+P*eta
    PE = P*(1-eta)+T*eta
    # error rate mu=1-epsilon-xi
    mu=1-eta
    
    phi_1=(1-(1-w)*p0)/((chi-1)*(RE-PE-delta)-eta/(mu-eta)*((RE-SE)+chi*(TE-RE)))
    phi_2=(1-(1-w)*p0)/((chi-1)*(RE-PE-delta)+mu/(mu-eta)*((RE-SE)+chi*(TE-RE)))
    phi_3=(w+(1-w)*p0)/((chi-1)*delta+mu/(mu-eta)*((TE-PE)+chi*(PE-SE)))
    phi_4=(w+(1-w)*p0)/((chi-1)*delta-eta/(mu-eta)*((TE-PE)+chi*(PE-SE)))
    
    phi_5=(1-p0)*(1-w)/((chi-1)*(RE-PE-delta)-eta/(mu-eta)*((RE-SE)+chi*(TE-RE)))
    phi_6=(1-p0)*(1-w)/((chi-1)*(RE-PE-delta)+mu/(mu-eta)*((RE-SE)+chi*(TE-RE)))
    phi_7=(1-w)*p0/((chi-1)*delta+mu/(mu-eta)*((TE-PE)+chi*(PE-SE)))
    phi_8=(1-w)*p0/((chi-1)*delta-eta/(mu-eta)*((TE-PE)+chi*(PE-SE)))
    
    return phi_1,phi_2,phi_3,phi_4,phi_5,phi_6,phi_7,phi_8

def cal2(args):# Check conditions of phi
    chi_list=[i for i in np.linspace(1,25,args.chi)]
    delta_list=[i for i in np.linspace(0,1,args.delta)]
    p0_list=[i for i in np.linspace(0,1,args.p0)]
    eta=args.eta
    
    delta_list2=[]# for result
    chi_list2=[]# for result
    p0_list2=[]# for result
    
    for delta in delta_list:
        progress=round(delta/delta_list[-1]*100)
        if int(progress)%20==0:
            print('{}%'.format(int(progress)))
        min_chi=100# temporary value
        tmp_delta=100# temporary value
        tmp_p0=100# temporary value
        for p0 in p0_list:
            for chi in chi_list:
                # Check conditions of phi
                phi_1,phi_2,phi_3,phi_4,phi_5,phi_6,phi_7,phi_8=cal(eta,delta,chi,args.w,p0)
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
        else:
            delta_list2.append(tmp_delta)
            chi_list2.append(min_chi)
            p0_list2.append(tmp_p0)
        
    write_csv(chi_list2,delta_list2,args)# output data
    #my_plot(chi_list2,delta_list2,eta,args.w)# output figure

# output csv data 
def write_csv(x,y,args):
    with open('./data/csv/discount/eta_{}_w_{}.csv'
              .format(str(args.eta).replace('.', ''),
              str(args.w).replace('.', '')), 'w') as f:
        
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows([x,y])

# output figure
def my_plot(x,y,eta,w):# generate the figure and setting of the figure
    plt.figure()
    plt.ylim(0,)
    plt.xlim(0,20)
    plt.xlabel('$\chi$')
    plt.ylabel('$\Delta$')
    plt.grid()
    plt.plot(x,y)
    
    plt.savefig('./data/figure/eta_{}_w_{}.png'
                .format(str(eta).replace('.', ''),
                        str(w).replace('.', '')))

if __name__ == "__main__":
    args = parse_args()# Parsing
    print('--------')
    print('Settings')
    print(' Payoff: (T,R,P,S)=({},{},{},{})'
          .format(payoff['T'],payoff['R'],payoff['P'],payoff['S']))
    print(' Probability: (w,eta)=({},{})'
          .format(args.w,args.eta))
    print(' Step_size: (delta,chi,p0)=({},{},{})'
          .format(args.delta,args.chi,args.p0))
    
    dt_start = datetime.datetime.now()
    print('start time: {}'.format(dt_start))
    
    T,R,P,S=payoff['T'],payoff['R'],payoff['P'],payoff['S']
    cal2(args)# main process
    
    dt_end = datetime.datetime.now()
    print('ending time: {}'.format(dt_end))
    print('<Calculating time: {}>'.format(dt_end-dt_start))
    print('--------')
    