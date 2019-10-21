chi=10
delta=10
p0=10

w_list=[0.99,0.95,0.9,0.85,0.8,0.75,0.7,0.65]
eta_list=[0.06,0.10,0.14,0.18,0.22,0.26]

for w in w_list:
	for eta in eta_list:
		print('--p0 {} --delta {} --chi {} --w {} --eta {}'.format(p0,delta,chi,eta,w))
