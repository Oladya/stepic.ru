S1 = input()

x = '('
y = ")"
count1 = S1.count(x)
count2 = S1.count(y)

if count1 == count2:
    print('ok')
else:
    print('bad')
   
