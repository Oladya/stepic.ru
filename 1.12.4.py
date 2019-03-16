

s = input()

if s == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print (s)



if s == "прямоугольник":
    a = int(input())
    b = int(input())
    print (a*b)



if s == "круг":
    r = int(input())
    print (3.14*r**2)
