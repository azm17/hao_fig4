#!/usr/bin/env python3
chi=1000
delta=1000
import numpy as np
step=0.001
eta_list=[round(i,3) for i in np.arange(step, 0.25+step, step)]

for eta in eta_list:
	print('--delta {} --chi {} --eta {}'.format(delta,chi,eta))
