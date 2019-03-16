
a = int(input())
b = int(input())
c = int(input())
d = int(input())

a <= b <= 10
c <= d <= 10

for i in range(c, d+1):
    print('\t', i, end='')
print()
    
for j in range(a, b+1):
    print(j, end='')
    for g in range(c, d+1):
        print('\t', g*j, end='')
    print()


#for k in range(c, d+1):
 #   print ("\t", c," ", d)

#for i in range (a, b+1):
 #   for j in range (c,d+1):
  #      print("\t", i*c,"", i*d)
   # print(i, end="")

        
       # print(i, i*d,end = '\t')
#print (c,d, end = " ")


       
#print(i, "\n")
 
    
    #for j in range(c , d):
        #print(a*c,end = '\t')
        #print(a*c,end = '\t')
   #print(b*d)

