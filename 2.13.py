


a = input()
a.sort()

cnt = 0
v = ""
for i in range(0, len(a)-1):
    cnt += 1
    if a[i] != a[i+1]:
        if cnt > 1:
            v += "{} ".format(a[i]) 
        cnt = 0

if cnt > 0:
    v += "{}".format(a[-1])

print(v)
