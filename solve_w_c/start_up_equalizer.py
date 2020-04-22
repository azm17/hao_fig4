#!/usr/bin/env python3
import numpy as np

# parameter
w = 1000
p1 = 1000
p4 = 1000

# parameter of error rate eta's step size
step = 0.001
eta_list = [round(i,3) for i in np.arange(0, 1/3 + step, step)]

for eta in eta_list:
	print(f'--p1 {p1} --p4 {p4} --w {w} --eta {eta}')
