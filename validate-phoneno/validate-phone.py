import re
test = int(input())
a = re.compile("[[9|8|7][0-9]{9}$")
for _ in range(0,test):
	num = str(input())
	if(a.match(num)):
		print("YES")
	else:
		print("NO")
