# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:43:36 2019

@author: azumi
"""
import csv

payoff={'T':1.5, 'R':1.0, 'P':0.0, 'S':-0.5}


def func_Eq67(w):
    T,R,P,S=payoff['T'],payoff['R'],payoff['P'],payoff['S']
    return max((R-S-w*(P-S))/(w*(T-P)-(T-R)),(T-P-w*(T-R))/(w*(R-S)-(P-S)))

# output csv data 
def write_csv(x,y):
    with open('./chi_c_noerror.csv', 'w') as f:
        
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows([x,y])

if __name__ == "__main__":
    w_list=[1,0.9,0.8,0.7,0.6,0.5,0.4]
    chi_c=[]
    for w in w_list:
        chi_c.append(func_Eq67(w))
    print(chi_c)
    write_csv(w_list,chi_c)
        