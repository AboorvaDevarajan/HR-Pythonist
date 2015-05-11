import re
test = int(input())
out=list()
for _ in range(0,test):
	e = input()
	exp = re.compile("[A-Za-z0-9_-]+[@][a-z|A-Z|0-9]+[.][a-zA-Z0-9]{1,3}$")
	if(exp.match(e)):
		out.append(e)
print(sorted(out))
