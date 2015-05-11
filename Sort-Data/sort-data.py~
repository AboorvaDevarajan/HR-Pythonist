from operator import itemgetter
nm = list(map(int,input().split()))
lst = list()
for _ in range(0,nm[0]):
	lst.append(list(map(int,input().split())))
k = int(input())
lst = (sorted(lst, key=itemgetter(k)))
for l in lst:
	for val in l:
		print(val,end="")
		print(" ",end="")
	print("")
