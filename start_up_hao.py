#!/usr/bin/env python3
chi=1000
delta=1000
import numpy as np

eta_list=[round(i,2) for i in np.arange(0.01, 0.31, 0.0001)]

for eta in eta_list:
	print('--delta {} --chi {} --eta {}'.format(delta,chi,eta))
