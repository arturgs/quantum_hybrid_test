from states.quantum_state import *

from scipy import sparse


class quantum_state_sparse(quantum_state):


	def apply_gate(self, gate, pos):
		if len(pos) == 1:		
			pos = [pos[0], pos[0]]
		g_0 = self.build_gate(gate, pos)
		self._state = g_0.dot(self._state)		
		return


	def exp_value(self, operator, pos):
		if len(pos) == 1:		
			pos = [pos[0], pos[0]]
		g_0 = self.build_gate(operator, pos)
		n = np.dot(np.transpose(np.conj(self._state)), g_0.dot(self._state))
		d = np.dot(np.transpose(np.conj(self._state)), self._state)
		return n/d


	
	def build_gate(self, gate, pos):
		gates = [sparse.identity(pow(base,pos[0])), sparse.csr_matrix(gate), sparse.identity(pow(base,self._N-pos[1]-1))]
		g_0 = gates[0]
		for pos in range(1,len(gates)):
			g_0 = sparse.kron(g_0, gates[pos])
		return g_0



