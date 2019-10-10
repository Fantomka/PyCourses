"""
# Задание 2. Уровень - диванный воин.
# Условие: необходимо написать программу,
# которая считывает с клавиатуры одно за
# другим два вещестенных числа operand_1 и operand_2,
# и затем строку. Если эта строка является обозначением одной из четырёх
# основных математических операций (+, -, * или /),
# то выведите результат применения этой
# операции к введенным ранее числам, в противном случае выведите «ЫЫЫЫЫЫ».
# Также «ЫЫЫЫЫЫ» следует вывести, если пользователь захочет поделить на ноль.

# Пример:
# Ввод:                                                              # Вывод:
# 23.5
# 55.2
# ЙЦУКЕН                                                             ЫЫЫЫЫЫ


# 23.5
# 0
# /                                                                  ЫЫЫЫЫЫ


# 20.1
# 10.1
# +                                                                  30.2
"""

def noob_calculator(operand_1, operand_2, operator):
    """
    operand_1, operand_2 - operands
    operator - (+, - /, *)
    """
    res = 0
    if operator == '+':
        res = round(float(operand_1) + float(operand_2), 1)
    elif operator == '-':
        res = round(float(operand_1) - float(operand_2), 1)
    elif operator == '*':
        res = round(float(operand_1) * float(operand_2), 1)
    elif operator == '/':
        try:
            res = round(float(operand_1) / float(operand_2), 1)
        except ZeroDivisionError:
            res = 'ЫЫЫЫЫЫ'
    res = 'ЫЫЫЫЫЫ'
    return res



if __name__ == '__main__':
    OP1 = input('write operand1: ')
    OP2 = input('write operand1: ')
    OPERATOR = input('write operator: ')
    print(noob_calculator(OP1, OP2, OPERATOR))
