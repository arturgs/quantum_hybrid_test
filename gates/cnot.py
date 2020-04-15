from gates.quantum_gate import *


class cnot_gate(quantum_gate):

	def __init__(self):
		self._gate = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
		return


