


s = "(1234)(544)"

val = 0
for a in s:

    if a == "(":
        print ("open")
        continue

    if a == ")":
        print ("close")
        continue

    val = val * 10
    val = val + int(a)



print("value ", val)
    
    
