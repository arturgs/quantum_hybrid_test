from gates.quantum_gate import *
import numpy as np


class sx_gate(quantum_gate):

	def __init__(self):
		self._gate = np.array([[0,1],[1,0]])
		return


		

