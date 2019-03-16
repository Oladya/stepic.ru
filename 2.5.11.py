

a = input()

b = []
splitted = a.split()
for i in splitted:
    b.append( int(i) )
    

#b = [int(i) for i in a.split()]

print(b)

cnt = 0
for i in range(0, len(b)):
    cnt += b[i]


print (cnt)
