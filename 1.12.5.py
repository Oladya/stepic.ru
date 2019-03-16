


a = int(input())
b = int(input())
c = int(input())


val_max = a
val_min = a
val_sum = a + b + c

if b > val_max:
    val_max = b

if c > val_max:
    val_max = c


if b < val_min:
    val_min = b

if c < val_min:
    val_min = c

other = val_sum - (val_max + val_min)
print (val_max)
print (val_min)
print (other)











