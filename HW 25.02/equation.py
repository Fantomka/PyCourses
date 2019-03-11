from math import sqrt


a = float(input("ВВедите коэффициент A: "))
b = float(input("ВВедите коэффициент B: "))
c = float(input("ВВедите коэффициент C: "))


if a != 0.0 and b != 0.0 and c != 0.0:
    discriminant = b * b - 4 * a * c
    if discriminant == 0.0:
        print(f"X1:{-b / (2 * a)}")
    elif discriminant > 0:
        print(f"X1:{(-b - sqrt(discriminant)) / (2 * a)} X2:{(-b + sqrt(discriminant)) / (2 * a)}")
elif a == 0.0 and b != 0.0:
    print(f"X1:{-(c / b)}")
elif a != 0.0 and b == 0.0:
    if c > 0.0:
        print(f"X1:{-sqrt(-c / a)} X2:{sqrt(-c / a)}")
    elif c == 0:
        print(f"X1:0")
