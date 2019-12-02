#!/usr/bin/env python3
w=1000
p1=1000
p4=1000
import numpy as np


step=0.001
<<<<<<< HEAD
eta_list=[round(i,3) for i in np.arange(0.15,1/3+step,step)]
=======
eta_list=[round(i,3) for i in np.arange(0.2,1/3+step,step)]
>>>>>>> 6f13e16fe32bee755eabc088de1588a7ff56979e

for eta in eta_list:
	print(f'--p1 {p1} --p4 {p4} --w {w} --eta {eta}')
