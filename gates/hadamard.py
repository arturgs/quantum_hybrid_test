from gates.quantum_gate import *
import numpy as np


class hadamard_gate(quantum_gate):

	def __init__(self):
		self._gate = np.array([[1,1],[1,-1]])		
		return

		

