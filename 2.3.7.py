


a, b = (int(i) for i in input().split())

s = 0
j = 0
for i in range(a, b+1):
    if i%3 == 0:
        j+=1
        s+=i
print (s/j)

