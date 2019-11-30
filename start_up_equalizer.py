#!/usr/bin/env python3
w=100
p1=100
p4=100
import numpy as np


step=0.001
eta_list=[round(i,3) for i in np.arange(0,0.25+step,step)]

for eta in eta_list:
	print(f'--p1 {p1} --p4 {p4} --w {w} --eta {eta}')
