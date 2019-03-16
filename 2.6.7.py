

s = input()
d = s.split()
b = []

for i in d:
    b.append(int(i))

sm = 0
qw = 0
for i in b:
    sm = sm + i
    qw = qw + (i*i)
    if sm == 0:
        print(qw)

    

