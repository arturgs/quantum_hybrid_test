from gates.quantum_gate import *


class cxx4_gate(quantum_gate):

	def __init__(self):
		sx = np.array([[0,1],[1,0]])
		gates = [sx,np.identity(4), sx]
		g_0 = gates[0]
		for pos in range(1,len(gates)):
			g_0 = np.kron(g_0, gates[pos])
		self._gate = g_0
		


