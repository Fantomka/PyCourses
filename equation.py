from math import sqrt


a = float(input("ВВедите коэффициент A: "))
b = float(input("ВВедите коэффициент B: "))
c = float(input("ВВедите коэффициент C: "))

if a == 0.0:
    print(f"X1:{-(c/b)}")
elif b == 0.0:
    print(f"X1:{-sqrt(-c/b)} X2:{sqrt(-c/b)}")
else:
    discriminant = b*b-4*a*c
    if discriminant == 0.0:
        print(f"X1:{-b/(2*a)}")
    elif discriminant > 0:
        print(f"X1:{(-b-sqrt(discriminant))/(2*a)} X2:{(-b+sqrt(discriminant))/(2*a)}")
