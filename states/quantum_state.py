import numpy as np
base = 2



'''
	FULLY QUANTUM MODE: python simulator of a Quantum state

'''

class quantum_state(object):

	def __init__(self, N):
		self._N = N
		self._hilbert_size = pow(2,N)
		self.zero_state()
		return


	def empty_state(self):
		self._state = np.zeros(self._hilbert_size, dtype=np.complex64)
		return


	def zero_state(self):
		self.empty_state()
		self._state[0] = 1
		return


	def one_state(self):
		self.empty_state()
		self._state[-1] = 1
		return


	def random_state(self):
		return


	def apply_op(self, operator):
		return


	def apply_gate(self, gate, pos):
		if len(pos) == 1:		
			pos = [pos[0], pos[0]]
		g_0 = self.build_gate(gate, pos)
		self._state = np.dot(g_0, self._state)		
		return

	
	def norm(self):
		return


	def normalize(self):
		return	

	
	def exp_value(self, operator, pos):
		if len(pos) == 1:		
			pos = [pos[0], pos[0]]
		g_0 = self.build_gate(operator, pos)
		n = np.dot(np.transpose(np.conj(self._state)), np.dot(g_0, self._state))
		d = np.dot(np.transpose(np.conj(self._state)), self._state)
		return n/d


	def __str__(self):
		return str(self.squares())		

	def squares(self):
		return np.multiply(np.conj(self._state), self._state)



	def build_gate(self, gate, pos):
		gates = [np.identity(pow(base,pos[0])), gate, np.identity(pow(base,self._N-pos[1]-1))]
		g_0 = gates[0]
		for pos in range(1,len(gates)):
			g_0 = np.kron(g_0, gates[pos])
		return g_0
		
	
