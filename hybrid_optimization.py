import numpy as np
import sys
sys.path
sys.path.append('..')

import gates.sx as sx
import gates.sz as sz
import gates.cnot as cnot
import states.quantum_state as state
import gates.hadamard as had
import optimizations.spsa as spsa
import gates.q2_gate as q2
from scipy import sparse
import cProfile
import re


'''
	FULLY QUANTUM MODE: define Quantum operation to be optimized
	This code is a simulation in python of the inner operation of a Quantum device.
	We fix the number of Quantum particles to N=6. The complexity of this code increases exponentially with N.
'''

def ising_1D_XX_Z(angles, N = 6, field = 0):

	# init circuit and gates
	# full version
	qs, h, cn, x, z, xx = full_ising_ini(N)
	
	# apply iteration gate sequence
	for i in range(2):
		# apply euler rotations
		for j in range(N):
			qs.apply_gate(x.rotate(angles[3*j+0]),[j])
			qs.apply_gate(z.rotate(angles[3*j+1]),[j])
			qs.apply_gate(x.rotate(angles[3*j+2]),[j])
		for k in range(N-1):
			qs.apply_gate(cn.raw(),[k,k+1])

	# compute energy
	energy = 0
	for m in range(N-1):		
		energy += qs.exp_value(xx.raw(), [m,m+1])
	energy = np.real(energy)
	print('Energy evaluation = ', energy)
	return energy


'''
	FULLY QUANTUM MODE: initialize Quantum device
'''

def full_ising_ini(N): 
	qs = state.quantum_state(N)
	h = had.hadamard_gate()
	cn = cnot.cnot_gate()
	x = sx.sx_gate()
	z = sz.sz_gate()
	xx = q2.q2_gate([x.raw(),x.raw()])
	return qs, h, cn, x, z, xx


'''
	HYBRID operation: 
	a classical optimization using a function call to Quantum operations (ising_1D_XX_Z) on a Quantum device
	The optimizator (SPSA) runs on a clssical device, and only function evaluations are submitted to the Quantum device.
	The operations of the Quantum device are parametrized by a set of classical parameters, determining the inner working
	of the classical device (imagine this set a hyperparameters). Once the Quantum device performs the function evaluation, it returns 
	the funtion result.
	The function spsa.step iterates this process fort a number of evaluations, passing to the Quantum device each function evaluation.
	Finally, the optimal set of parameters minimizing the objective function are returned.
'''

def hybrid_optimization():
	'''
	CLASSICAL SECTION: define optimizator and initialize classical code
	'''
	# SPSA parameters	
	a = 0.01
	c = 0.001
	alpha = 0.602
	gamma = 0.101
	iters = 3000
	A = 50/iters
	
	# initial optimization parameters
	N = 7
	n_params = 4*N - 1
	theta = 0.1*np.ones(n_params)
	theta_max = (np.pi/2)*np.ones(n_params)
	theta_min = (-np.pi/2)*np.ones(n_params)

	# solve opt
	opt = spsa.spsa(A, a, c, alpha, gamma, theta, theta_max, theta_min, iters)
	'''
	HYBRID SECTION: spsa.step repetedly calls a function evaluation on the quantum device.
	'''
	l_p, l_m = opt.step(ising_1D_XX_Z)


if __name__ == '__main__':
	
	cProfile.run('hybrid_optimization()')



