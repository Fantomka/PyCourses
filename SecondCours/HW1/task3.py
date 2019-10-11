"""
# Задача 3. Уровень - шахматный мачо.
# Условие: в шахматах конь ходит буквой Г.
# В школе BPS есть особый конь на шахматной доске: он тоже ходит буквой Г,
# только по горизонтали он может пройти 2 клетки,
# а по вертикали 5, или наоборот. Даны две различные клетки шахматной доски.
# Требуется определить,
# возможно ли конем из школы BPS перейти из одной клетки шахматной доски в другую.

# Входные данные : 4 целых числа (все > 0).
# В первой строке вводится номер столбца 1 клетки. На второй строке - номер
# строки первой клетки.
# Потом аналогично на третьей и четвертой строках вводится информацию о 2 клетке.

# Выходные данные: "YESSSS!" если такой ход возможен, "No no" - если такой ход невозможен.

# Пример:
# Ввод:                                              # Вывод:
# 1
# 1
# 4
# 3                                                  No no

# 3
# 6
# 1
# 1                                                  YESSSS!
"""


def check_horse_move(x_1, y_1, x_2, y_2):
    """
         checks first 4 digits,
         if horse can move from x_1, y_1
         to x_2, y_2 - then returns YESSSS!
         else returns No no
    """
    if max(x_1, x_2) - min(x_1, x_2) == 2 and max(y_1, y_2) - min(y_1, y_2) == 5 or \
       max(x_1, x_2) - min(x_1, x_2) == 5 and max(y_1, y_2) - min(y_1, y_2) == 2:
        return 'YESSSS!'
    return 'No no'


if __name__ == '__main__':
    X1_COORD = int(input('write first x: '))
    Y1_COORD = int(input('write first y: '))
    X2_COORD = int(input('write second x: '))
    Y2_COORD = int(input('write second y: '))
    print(check_horse_move(X1_COORD, Y1_COORD, X2_COORD, Y2_COORD))
