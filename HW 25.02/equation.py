from math import sqrt
import sys


def equation(a, b, c):
    if a != 0.0 and b != 0.0 and c != 0.0:
        discriminant = b * b - 4 * a * c
        if discriminant == 0.0:
            return -b / (2 * a)
        elif discriminant > 0:
            return (-b - sqrt(discriminant)) / (2 * a), (-b + sqrt(discriminant)) / (2 * a)
    elif a == 0.0 and b != 0.0:
        return -(c / b)
    elif a != 0.0 and b == 0.0:
        if c < 0.0:
            return [(-sqrt(-c / a)), (sqrt(-c / a))]
        elif c == 0:
            return 0


if __name__ == '__main__':
    print(sys.path)
    A = float(input("ВВедите коэффициент A: "))
    B = float(input("ВВедите коэффициент B: "))
    C = float(input("ВВедите коэффициент C: "))
    print(equation(A, B, C))
