
a = int(input("Recommended hours of sleeping"))
b = int(input("Too much hours of sleeping"))
h = int(input("Enter hours of sleeping"))

if a < h < b:
    print("Это нормально")
elif h < a and a <= b:
    print ("Недосып")
elif h > b and a <= b:
    print("Пересып")
