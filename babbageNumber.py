#https://programmingpraxis.com/2018/10/09/babbages-number/
smallnumberbelow,postfix = 99736, "269696"
n,minimum = smallnumberbelow -1,-1
while True:
	sqr = n**2
	if str(sqr).endswith(postfix):minimum = n
	if sqr < 269696:break
	n -=1
print minimum