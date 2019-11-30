# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 00:59:35 2019

@author: Azumi Mamiya

Find minimum discount factor of equalizer under observation errors numerically


Please enter the following to execution this code.
$ python3 wc_equalizer.py -eta 0.1 -p1 1000 -p4 1000 -w 1000 
or
$ python3 wc_equalizer.py

if you enter the latter,
please change value of parameters in the python's dict "default_settings" .


"""

import matplotlib.pyplot as plt
from argparse import ArgumentParser
import numpy as np
import csv

# --parameter setting (default)--
default_settings={'p1':100,# step size of p1 ,0<=p1<=1
                  'p4':100,# step size of p4 ,0<=p4<=1
                  'w':100,# step size of discount factor w
                  'eta':0.1}# error rate eta=epsilon+xi

payoff={'T':1.5, 'R':1.0, 'P':0.0, 'S':-0.5}
# --- ---

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--p1', metavar='p1_StepSize',
                        type=float, 
                        default=default_settings['p1'])
    
    parser.add_argument('--p4', metavar='p4_StepSize',
                        type=float, 
                        default=default_settings['p4'])
    
    parser.add_argument('--w', metavar='w_StepSize',
                        type=float,
                        default=default_settings['w'])
    
    parser.add_argument('--eta', metavar='error_rate_eta',
                        type=float,
                        default=default_settings['eta'])
    
    args = parser.parse_args()
    return args

def p2(payoff_vector,eta,w,p1,p4):
    R,S,T,P=payoff_vector
    RE = R*(1-eta)+S*eta
    SE = S*(1-eta)+R*eta
    TE = T*(1-eta)+P*eta
    PE = P*(1-eta)+T*eta
    mu=1-eta
    
    p2=(p1*(mu*(TE-PE)-eta*(RE-SE))-(1/w+p4)*(TE-RE))/(mu*(RE-PE)-eta*(TE-PE))
    
    return p2

def p3(payoff_vector,eta,w,p1,p4):
    R,S,T,P=payoff_vector
    RE = R*(1-eta)+S*eta
    SE = S*(1-eta)+R*eta
    TE = T*(1-eta)+P*eta
    PE = P*(1-eta)+T*eta
    mu=1-eta
    
    p3=((1/w-p1)*(PE-SE)+p4*(mu*(RE-SE)-eta*(TE-PE)))/(mu*(RE-PE)-eta*(TE-PE))
    
    return p3

def my_plot(x,y):
    plt.plot(x,y,'o',markersize=3)
    plt.ylabel(r"$w_c$",fontsize=18)
    plt.xlabel(r"$\epsilon+\xi$",fontsize=18)
    plt.grid()
    plt.xlim(0,1)
    plt.ylim(0, 1)
    
def write_csv(x,y,args):
    with open('./data/w_c/eta_{}.csv'
              .format('{:.3f}'.format(args.eta).replace('.', '')), 'w') as f:
        
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows([x,y])

if __name__ == "__main__":
    args = parse_args()# Parsing
    payoff_vector=payoff['R'],payoff['S'],payoff['T'],payoff['P']
    
    list_w=[]
    w_l=np.linspace(0,1,args.w)
    w_l=w_l[int(args.w*0.35):]
    p1_list=np.linspace(0,1,args.p1)
    p4_list=np.linspace(0,1,args.p4)
    
    eta=args.eta
    print(f'----eta={eta}----')
    #for eta in eta_list:
    w_c=100# temporary value
    count_w=0
    count_w_max=len(w_l)
    tmp_p1=-1
    tmp_p4=-1
    for w in w_l:
        count_w+=1
        print(f'{round(count_w/count_w_max*100,1)}%')
        for p1 in p1_list:
            for p4 in p4_list:
                p2_v=p2(payoff_vector,eta,w,p1,p4)
                p3_v=p3(payoff_vector,eta,w,p1,p4)
                if p2_v>=0 and p3_v>=0:
                    if w_c>=w:
                        w_c=w
                        tmp_p1=p1
                        tmp_p4=p4
        #list_w.append(w_c)

    print(f'eta:{eta},w_c:{w_c},p1:{tmp_p1},p4:{tmp_p4}')
    write_csv([eta],[w_c],args)
    
