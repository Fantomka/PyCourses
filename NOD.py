def gcd(a: int, b: int) -> int:
    for i in range(min(a, b), 0, -1): #идем от меньшего числа чтобы избежать лищних итераций
        if (a % i) == 0 and (b % i) == 0:
            return i
