#programmming praxis
from itertools import count
from math import sqrt
for n in range(1,1000000):
	two = []
	for i in range(int(sqrt(n))+1):
		prev3,prev4 =0,0
		for j in count(2):
			two = []
			p = i**j
			if p > n:
			 	break
			rem = n - p
			if p == prev3 and rem == prev4:
				break
			prev3 = p
			prev4 = rem			
			two.append((i,j,p))
			for m in range(1,int(sqrt(rem))+1):
				prev1, prev2 = 0,0
				for k in count(2):			
					othr = m**k
					if prev1== othr and prev2 == rem:
						break
					prev1,prev2 =othr,rem
					if othr > rem:
						break
					if othr == rem:						
						two.append((m,k,rem))					
						break				
			
			if len(two) ==2:
				break
		if len(two) ==2:
				break
	if two:
		print n,"=",two[0][0],"^",two[0][1],"+",two[1][0],"^",two[1][1]