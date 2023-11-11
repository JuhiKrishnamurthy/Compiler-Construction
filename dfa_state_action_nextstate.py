import sys


def q0(c):
	if c == "b":
		nextstate=q0
	elif c == "a":
		nextstate=q1
	else:
		nextstate=qna

	return nextstate

def q1(c):
	if c == "b":
		nextstate=q2
	elif c == "a":
		nextstate=q1
	else:
		nextstate=qna

	return nextstate

def q2(c):
	if c == "b":
		nextstate=qf
	elif c == "a":
		nextstate=q1
	else:
		nextstate=qna

	return nextstate

def qf(c):
	if c == "b":
		nextstate=q0
	elif c == "a":
		nextstate=q1
	else:
		nextstate=qna

	return nextstate

def qna(c):
	return qna


def main():
	string = input("enter the string: ")
	ns=q0
	for ch in string:
		ns=ns(ch)
	if ns == qf:
		print("ACCEPTED")
	else:
		print("NOT ACCEPTED")

if __name__ == "__main__":
	main()
		


