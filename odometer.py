stringlist = ["G7TS39","Z9ZZ99","1Z9"]
for string in stringlist:
	index,carry = -1,-1
	s = list(string)
	while carry and (abs(index) <= len(string)):
		if s[index].isdigit():
			addn = int(s[index]) + 1
			s[index] = "0" if addn == 10 else str(addn)
			carry = 1 if addn == 10 else 0

		else:
			next = "A" if s[index] == "Z" else chr(ord(s[index])+1) 
			s[index] = "A" if next =="Z" else next
			carry = 1 if next =="A" else 0
		index -= 1

	print ''.join(s)
