import numpy as np

class quantum_gate():		


	def __init__(self):
		return


	def __str__(self):
		return str(self._gate)


	def raw(self):
		return self._gate

	
	def rotate(self, theta):
		dim = np.shape(self._gate)[0]
		if dim == 2:
			id_gate = np.array([[1,0],[0,1]]) 
		else:
			id_gate = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

		return np.cos(theta)*id_gate + 1.j*np.sin(theta)*self._gate

		

	def build(self, gates):
		self._gate = gates[0]
		for pos in range(1,len(gates)):
			self._gate = np.kron(self._gate, gates[pos])


	def r_prod(self, gate):
		self._gate = np.matmul(self._gate, gate)

