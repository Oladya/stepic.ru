

out = ""
s = "aaaaZbbbccc"
cnt = 0
for i in range(0, len(s)-1):
    cnt = cnt + 1
    if s[i] != s[i+1]:
        out += "{}{}".format(s[i], cnt)
        #print(s[i], cnt)
        cnt = 0


out += "{}{}".format(s[len(s)-1], cnt+1)

print(out)
