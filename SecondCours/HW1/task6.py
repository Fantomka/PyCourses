# Задание 6. Уровень - Кодзима, ты ли это?
# Условие: вы создали игру в жанре шутер. Теперь ваш дизайнер придумал новое неизвестное никому оружее - дробовик.
# Известно, что дробовики стреляют дробью (внезапно, правда?). Ваша задача - рассчитать суммарный урон, наненсенный
# выстрелом из дробовика.


# Входные данные : Сначала вводится количество дробинок.
# Затем урон от каждой дробинки. Урон от каждой дробинки выражается простой дробью,
# её числитель и знаменатель вводятся на отдельных строках.

# Выходные данные : Суммарный урон, выраженный простой несократимой дробью с дробной
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


from collections import namedtuple


FractionalNumber = namedtuple('FractionalNumber', 'dividend, divider')


def gcd(a: int, b: int) -> int:
    """
        returns greatest common divisor of 2 numbers
    """
    for i in range(min(a, b), 0, -1):    # идем от меньшего числа чтобы избежать лищних итераций
        if (a % i) == 0 and (b % i) == 0:
            return i


def shotgun_dmg(fractions: list):
    """
        returns fraction of summary damage
    """
    dividend = 0
    divider = 1
    for i in range(len(fractions)):
        divider *= fractions[i].divider
    for i in range(len(fractions)):
        dividend += fractions[i].dividend * (divider / fractions[i].divider)
    return FractionalNumber((dividend / gcd(int(dividend), divider)), (divider / gcd(int(dividend), divider)))


if __name__ == '__main__':
    total = []
    for i in range(int(input('print count of fractions: '))):
        dmg = FractionalNumber(int(input(str(i+1) + ' dividend: ')), int(input(str(i+1) + ' divider: ')))
        total.append(dmg)
    dmg = shotgun_dmg(total)
    print("{0}/{1}".format(int(dmg.dividend), int(dmg.divider)))
 

