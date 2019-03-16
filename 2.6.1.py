


s = input()
spl = s.split()
b = []
for i in spl:
    b.append(int(i))

m = b[0]

for x in b:
    if m > x:
          m = x

print(m)


