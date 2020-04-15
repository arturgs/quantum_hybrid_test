import numpy as np
import random



'''
	Implemetation of SPASA optimizator as in https://www.jhuapl.edu/SPSA/
'''

class spsa():

	def __init__(self, A, a, c, alpha, gamma, theta, theta_max, theta_min, iters):
		self._A = A
		self._a = a
		self._c = c
		self._alpha = alpha
		self._gamma = gamma
		self._iters = iters
		self._theta = theta
		self._theta_max = theta_max
		self._theta_min = theta_min

	def get_theta(self):
		return self._theta


	def set_theta(self, theta):
		self._theta = theta


	def step(self, loss, *args):
		l_p = []
		l_m = []
		num_p = self._theta.shape[0]
		for k in range(self._iters):
			ak = self._a/(k+1+self._A)**self._alpha
			ck = self._c/(k+1)**self._gamma
			delta = (np.random.randint(0, 2, num_p) * 2 - 1)
			theta_p = np.add(self._theta, ck*delta)
			theta_m = np.add(self._theta, -ck*delta)
			theta_p = self.bounds(theta_p)
			theta_m = self.bounds(theta_m)
			y_p = loss(theta_p, *args)
			y_m = loss(theta_m, *args)
			l_p.append(y_p)
			l_m.append(y_m)
			g = np.divide(y_p - y_m, 2*ck*delta)
			self._theta = np.add(self._theta, -ak*g)
			'''
			err = np.abs((y_p-y_m)/y_p)
			print(err)
			if (err<1e-10):
				break
			'''
		return l_p, l_m 

	def bounds(self, theta):
		theta = np.maximum(theta, self._theta_min)
		theta = np.minimum(theta, self._theta_max)
		return theta
		
		
		
	


# test SPSA with THE Rosenbrock function

if __name__ == '__main__':

	def rosenbrock(x):
		a = 1
		b = 10
		return a*np.power(a-x[0],2) + b*np.power(x[1]-np.power(x[0],2),2)


	a = 0.0002
	c = 0.1
	alpha = 0.602
	gamma = 0.101
	theta = np.array([10.1,8.3])
	theta_max = np.array([100, 100])
	theta_min = np.array([-100, -100])
	iters = 300
	A = 30
	opt = spsa(A, a, c, alpha, gamma, theta, theta_max, theta_min, iters)
	opt.step(rosenbrock)
	
