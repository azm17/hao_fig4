#!/usr/bin/env python3
chi=1000
delta=1000
p0=1000

w_list=[0.99,0.95,0.9,0.85,0.8,0.75,0.7,0.65]
w_list=[i-0.025 for i in w_list]
eta_list=[0.06,0.10,0.14,0.18,0.22,0.26]

for w in w_list:
	for eta in eta_list:
		print('--p0 {} --delta {} --chi {} --w {} --eta {}'.format(p0,delta,chi,w,eta))
