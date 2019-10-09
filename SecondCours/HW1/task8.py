# Задание 8. Уровень - жестоко.

# Условие: напишите программу, которая для данного текста подсчитывает частоты всех символов в нем.
# Регистр не важен. То есть символы 'А' и 'а' - эквивалентны.

# Входные данные: произвольный текст.

# Выходные данные: таблица с частотами символов.
# Таблица должна быть отсортирована по убыванию частот, в случае равных частот — в алфавитном порядке.
# Если в тексте нет алфавитных символов - выводим перенос строки.

# Пример:
# Ввод:                                      # Вывод:
# hello, world!                              l: 3
#                                            o: 2
#                                            d: 1
#                                            e: 1
#                                            h: 1
#                                            r: 1
#                                            w: 1


from operator import itemgetter


def frequency_analysis(message):
    """
         returns periodicity of letters in message
    """
    letters = {}
    for i in message:
        if i.isalpha() is True:
            if letters.get(i) is None:
                letters[i] = 1
            else:
                letters[i] += 1
    letters = letters.items()
    letters = sorted(letters, key=itemgetter(0))
    letters = sorted(letters, key=itemgetter(1), reverse=True)
    return letters


if __name__ == '__main__':
    print(frequency_analysis(input('print message: ').lower()))