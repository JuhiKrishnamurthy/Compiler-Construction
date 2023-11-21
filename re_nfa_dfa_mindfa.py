import sys
re = "(a|b)*abb"

def prod_fn(f,g):
	def f_cross_g(x,y):
		return (f(x), g(y))
	return f_cross_g

class nfa:
	def __init__(self,re_exp):
		self.re_exp = re_exp
	

	def union(self, a, b):

		def q0(inp):
			return prod_fn(q1,q2)

		def q1(inp):
			if inp == a:
				return q3
			else:
				return qd

		def q2(inp):
			if inp == b:
				return q4
			else:
				return qd

		def q3(inp):
			return qf

		def q4(inp):
			return qf

		def qf(inp):
			return qf

		def qd(inp):
			return qd

	def kleene_closure(self, a):

		def q0(inp):
			return q1,qf

		def q1(inp):
			if inp == a:
				return q2
			else:
				return qd

		def q2(inp):
			return q1,qf

		def qf(inp):
			return qf

		def qd(inp):
			return qd

	def concat(self, a, b):

		def q0(inp):
			if inp==a:
				return q1
			else:
				return qd

		def q1(inp):
			if inp==b:
				return qf
			else:
				return qd

		def qf(inp):
			return qf

		def qd(inp):
			return qd









