from gates.quantum_gate import *
import numpy as np


class q2_gate(quantum_gate):

	def __init__(self, gates):
		self._gate = gates[0]
		for pos in range(1,len(gates)):
			self._gate = np.kron(self._gate, gates[pos])

		return
