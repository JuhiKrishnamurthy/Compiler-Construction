import sys
import json

"""
state_dict: it is a dict
{
	name: tuple of strings, immutable
	is_initial = bool
	is_final = bool
	is_dead = bool
}
"""

class state:
	def __init__(self,json_state):
		self.name = tuple(json_state["name"])
		self.is_initial = json_state["is_initial"]
		self.is_final = json_state["is_final"]
		self.is_dead = json_state["is_dead"]

		return

"""
autamata spec json file structure
{
	type:"nfa"|"epsilon-nfa"|"dfa" (string)
	alphabets:[set of unique tokens. "epsilon" is a restricted token]
	states: [ set of unique state objects, "phi" is a restricted state name used for dead state]
	transitions : dict, key = tuple of state_name and token, value = set of final state names

}
"""

class automata:
	def __init__(self,nfa_json_file_name):
		self.spec=json.load(open(nfa_json_file_name))

		self.automata_type = self.spec["type"]

		self.alphabets = self.spec["alphabets"]

		self.state_name_state_dict = {}
		for s in self.spec["states"]:
			# each s is a dict
			tstate = state(s)
			self.state_name_state_dict[s["name"]] = tstate
		#print(self.state_name_state_dict)

		self.cur_state_names= None
		for s in self.state_name_state_dict:
			if (self.state_name_state_dict[s].is_initial == True):
				self.cur_state_names = [s]
				break

		self.transitions ={}
		for tr in self.spec["transitions"]:
			val_str = self.spec["transitions"][tr]
			val = tuple(val_str.split(","))
			tr = tuple(tr.split(","))
			self.transitions[tr] = val
		## make dead state transitions
		for a in self.alphabets:
			v = "phi"
			self.transitions[("phi",a)] = tuple(v.split(","))
		self.transitions[("phi","epsilon")] = tuple(v.split(","))

		#print(self.transitions)



	def next_states(self,x):
		next_state_names = set([])

		### epsilon closure
		for s in self.cur_state_names:
			eps_list = []
			if ((s, "epsilon") in self.transitions):
					eps_list = self.transitions[ (s, "epsilon")]
			for ns in eps_list:
				next_state_names.add(ns)
		self.cur_state_names = self.cur_state_names + list(next_state_names)


		for s in self.cur_state_names:
			ns_list =[]
			if ((s, x) in self.transitions):
				ns_list = self.transitions[ (s, x)]
			else:
				ns_list = tuple(["phi"])

			## get the epsilon transition list also
			eps_list = tuple([])
			if ((s, "epsilon") in self.transitions):
				eps_list = self.transitions[ (s, "epsilon")]

			ns_list = ns_list + eps_list
			for ns in ns_list:
				next_state_names.add(ns)
		self.cur_state_names = list(next_state_names)


	def in_accept_state(self):
		for s in self.cur_state_names:
			if (self.state_name_state_dict[s].is_final == True):
				return True
		return False

	def accept(self,x, delim=None):
		tokens = []
		if (delim == None):
			tokens = list(x)
		else:
			tokens = x.split(delim)
		for t in tokens:
			print(f"token:{t} cur states = {self.cur_state_names}")
			self.next_states(t)
			print(f"token:{t} cur states = {self.cur_state_names}")

		if (self.in_accept_state()):
			return True
		else:
			return False


	# def create_dfa():
	# 	dfa_spec = {}
	# 	dfa_spec["type"]="dfa"
	# 	dfa_spec["alphabets"] = self.alphabets
	# 	dfa_spec["states"] = []
	# 	dfa_spec["transitons"]={}


	# 	new_state_names = []

	# 	self.cur_state_names= None
	# 	for s in self.state_name_state_dict:
	# 		if (self.state_name_state_dict[s].is_initial == True):
	# 			self.cur_state_names = [s[0]]
	# 			break

	# 	for s in self.state_name_state_dict:
	# 		self.next_states("epsilon")
	# 		self.cur_state_names




def main():
	automata_json = sys.argv[1]
	nfa = automata(automata_json) 
	in_str = sys.argv[2]
	in_lang = nfa.accept(in_str)
	print(f"acceptance of string {in_str} : {in_lang}")
	return

if __name__ =="__main__":
	main()












