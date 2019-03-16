



s = input()
b = s.upper()
cnt = 0
for x in b:
    if x == "C" or x == "G":
        cnt+=1

d = len(b)

print((cnt/d)*100)
