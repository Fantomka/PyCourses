"""
# Задание 5. Уровень - математик.
# Условие: всегда интересно , является ли число простым.
# Простые числа - натуральные числа,
# которые имеют только 2 делителя : 1 и само это число
# (т.к. они обязаны отличаться - 1 это не простое число).
# Ваша задача вывести все делители числа N.
# В случае, если число N - простое, нужно дополнительно сообщить об этом.

# Входные данные: N - натуральное число (< 1000000).
# Выходные данные: все делители числа N в порядке возрастания.
# Если число N - простое, то еще вывести слово ACHTUNG

# Пример:
# Ввод:                                               # Вывод:
# 5                                                   1 5
#                                                     ACHTUNG

# 9                                                   1 3 9

# 13                                                  1 13
#                                                     ACHTUNG
"""


def check_divider(number):
    """
        returns list with dividers of N
        with word  ACHTUNG if N is prime number
    """
    res = []
    flag = None
    for i in range(1, number + 1):
        if number % i == 0:
            res.append(i)
    if len(res) == 2:
        flag = 'ACHTUNG'
    return res, flag


if __name__ == '__main__':
    RES, WARN = check_divider(int(input('print number: ')))
    for item in RES:
        print(str(item) + ' ', end='')
    print()
    if WARN is not None:
        print(WARN)
