#!/usr/bin/env python3
chi=1000
delta=1000
p0=1000
import numpy as np

#w_l=[round(i,2) for i in np.arange(0.88, 0.65, -0.01)]#tty ubuntu
#w_l=[round(i,2) for i in np.arange(0.99, 0.87, -0.01)]#azm ubuntu
w_l=[0.87]#ubuntu2
w_list1=[0.99,0.95,0.9,0.85,0.8,0.75,0.7,0.65]# workstation
#w_list2=[i-0.025 for i in w_list1]# azumi_ubuntu

w_list=set(w_l)-set(w_list1)
print(w_list)
eta_list=[0.06,0.10,0.14,0.18,0.22,0.26]


for w in w_list:
	for eta in eta_list:
		print('--p0 {} --delta {} --chi {} --w {} --eta {}'.format(p0,delta,chi,w,eta))
