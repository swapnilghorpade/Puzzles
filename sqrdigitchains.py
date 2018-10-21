#Project Euler Problem 92
#https://projecteuler.net/problem=92
numCntr = 0
for i in range(1,10000000):
	addition = 0
	number = i
	while True:
		addition = 0
		for c in str(number):
			addition+= int(c)**2
		number = addition
		if addition == 89 or addition == 1:
			if addition==89:
				numCntr += 1
			break
print numCntr