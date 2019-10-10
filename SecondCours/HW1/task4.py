"""
# Задание 4. Уровень - гросмейстер.
# Условие: Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга.

# Входные данные: программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.

# Выходные данные : eсли ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

# Пример:
# Ввод:                                        # Вывод:
# 1 7
# 2 4
# 4 8
# 3 2
# 8 5
# 7 3
# 6 1
# 5 6                                          NO
"""

def check_queens_collision(*args):
    """
    checks 8 queens positions, if one couple
    bit each other returns YES, else NO
    """
    for i in range(7):
        j = i + 1
        for j in range(i + 1, 7):
            if int(args[i][0]) == int(args[j][0]) or int(args[i][1]) == int(args[j][1]) or  \
           max(int(args[i][0]), int(args[j][0])) - min(int(args[i][0]), int(args[j][0])) == \
           max(int(args[i][1]), int(args[j][1])) - min(int(args[i][1]), int(args[j][1])):
                return 'YES'
    return 'NO'


if __name__ == '__main__':
    MAS = []
    for coord in range(8):
        MAS.append(input(str(coord + 1) + " queen's coords: ").split())
    print(check_queens_collision(*MAS))
