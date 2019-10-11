"""
# Задание 6. Уровень - Кодзима, ты ли это?
# Условие: вы создали игру в жанре шутер.
# Теперь ваш дизайнер придумал новое неизвестное никому оружее - дробовик.
# Известно, что дробовики стреляют дробью (внезапно, правда?).
# Ваша задача - рассчитать суммарный урон, наненсенный
# выстрелом из дробовика.

# Входные данные : Сначала вводится количество дробинок.
# Затем урон от каждой дробинки.
# Урон от каждой дробинки выражается простой дробью,
# её числитель и знаменатель вводятся на отдельных строках.

# Выходные данные : Суммарный урон,
# выраженный простой несократимой дробью с дробной
# чертой между числителем и знаменателем.

# Пример:
# Ввод:                                               # Вывод:
# 2
# 1
# 50
# 3
# 20                                                 17/100

# 3
# 1
# 50
# 2  1
# 40 20
# 3  1
# 30 10                                                17/100
"""

from collections import namedtuple


FractionalNumber = namedtuple('FractionalNumber', 'dividend, divider')


def gcd(first: int, second: int):
    """
        returns greatest common divisor of 2 numbers
    """
    for i in range(min(first, second), 0, -1):           # идем от меньшего числа,
        if (first % i) == 0 and (second % i) == 0:    # чтобы избежать лищних итераций
            return i
    return None


def shotgun_dmg(fractions: list):
    """
        returns fraction of summary damage
    """
    dividend = 0
    divider = 1
    for _, item in enumerate(fractions):
        divider *= item.divider
    for _, item in enumerate(fractions):
        dividend += item.dividend * (divider // item.divider)
    return FractionalNumber((dividend / gcd(dividend, divider)), (divider / gcd(dividend, divider)))


if __name__ == '__main__':
    TOTAL = []
    for counter in range(int(input('print count of fractions: '))):
        DMG = FractionalNumber(int(input('dividend: ')), int(input('divider: ')))
        TOTAL.append(DMG)
    DMG = shotgun_dmg(TOTAL)
    print("{0}/{1}".format(int(DMG.dividend), int(DMG.divider)))
