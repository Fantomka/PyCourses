"""
# Задание 7. Уровень - знаток алгоритмов.
# Условие: Напишите программу, которая проверяет,
# является ли скобочная последовательность правильной

# Под скобками понимается следующие символы: "(", ")", "{", "}", "[", "]".

# Входные данные: в первой строке идет число n,
# а потом идет n строк,
# в каждой из них — скобочная последовательность.

# Выходные данные: для каждой скобочной
# последовательности на
# отдельной строке выведите "yes" если
# она является правильной и "no" в противном случае.

# Замечание: реализовать решение при помощи стэка.


# Пример:
# Ввод:                                        # Вывод:
# 4
# ][                                           no
# [({})]                                       yes
# [(])                                         no
# ()                                           yes
"""


class Stack:
    """
        Simple realisation of Stack
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
            Return True if Stack is empty
            else returns False
        """
        return self.items == []

    def push(self, item):
        """
            appends item at the end of Stack
        """
        self.items.append(item)

    def pop(self):
        """
             delete last item in Stack
        """
        return self.items.pop()

    def peek(self):
        """
            returns last item of Stack
        """
        return self.items[len(self.items)-1]

    def size(self):
        """
            returns real size of stack (not last index)
        """
        return len(self.items)

    def free(self):
        """
            clearing stack
        """
        self.items = []


if __name__ == '__main__':
    SEQUENCE = Stack()
    for i in range(int(input('count of sequences: '))):
        flag = True
        for j in input('SEQUENCE: '):
            if j in ('(', '[', '{'):
                SEQUENCE.push(j)
            elif SEQUENCE.is_empty() is True:
                flag = False
                break
            elif j == ')' and SEQUENCE.peek() == '(':
                SEQUENCE.pop()
            elif j == '}' and SEQUENCE.peek() == '{':
                SEQUENCE.pop()
            elif j == ']' and SEQUENCE.peek() == '[':
                SEQUENCE.pop()
            else:
                flag = False
        if flag is False:
            print('no')
            SEQUENCE.free()
        else:
            print('yes')
            SEQUENCE.free()
