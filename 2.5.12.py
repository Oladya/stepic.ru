s = input()
spl = s.split()

# s = "4 5 6"
# spl = ["4", "5", "6"]

b = []

for i in spl:
    b.append(int(i))


if len (b) == 1:
    print (s)
    exit(0)



c = []
c.append(b[-1] + b[1])


for i in range(1, len(b)-1):
    c.append(b[i-1] + b[i+1])


c.append(b[-2] + b[0])

v = ""

for i in c:
    v += "{} ".format(i)
    
print(v)
