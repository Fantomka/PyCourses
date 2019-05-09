"""Модуль для решения квадратного уравнения v2.0"""

from math import sqrt


def solve_quadratic(a, b, c):
    """Решение квадратного уравнения"""
    if b == 0 and c == 0:
        return (0,)
    elif b == 0 and c < 0:
        return -sqrt(-c/a), sqrt(-c/a)
    elif b != 0 and c == 0:
        return 0, -b/a
    # Решение полного квадратного уравнения
    dis = (b ** 2) - (4 * a * c)
    if dis > 0:
        return (-b+sqrt(dis))/(2*a), (-b-sqrt(dis))/(2*a)
    elif dis == 0:
        return (-b/(2*a),)
    return None


def solve_linear(b, c):
    """Решение линейного уравнения"""
    if b != 0:
        return (-c/b,)
    return None


def get_roots(a, b, c):
    """Получаем корни из уравения вида ax^2 + bx + c = 0"""
    if a != 0:
        return solve_quadratic(a, b, c)
    else:
        return solve_linear(b, c)


if __name__ == '__main__':
    A = float(input("ВВедите коэффициент A: "))
    B = float(input("ВВедите коэффициент B: "))
    C = float(input("ВВедите коэффициент C: "))
    print(get_roots(A, B, C))
