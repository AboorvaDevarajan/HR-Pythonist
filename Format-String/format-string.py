n = int(input())
out = list()
for i in range(2,n+1):
    a = list()
    a.append(str(i))
    a.append(str(oct(i))[2:])
    a.append(str(hex(i))[2:])
    a.append(str(bin(i))[2:])
    out.append(a)
multtable = [y]+[[i]+map(partial(operator.add,i),y[1:]) for i in x]
for i in multtable:
    for j in i:
        print str(j).rjust(3),
    print
