"""
Этот модуль реализует словарь синонимов с командами:
add word1 word2
count word
check word1 word2
"""


def syn_func():
    synonyms = {}
    for i in range(int(input('number of commands: '))):
        command = input(f'command {i+1}: ').lower().split()
        if command[0] == 'add':
            if synonyms.get(command[1]) is None:
                synonyms[command[1]] = []
            if synonyms.get(command[2]) is None:
                synonyms[command[2]] = []
            if command[2] not in synonyms.get(command[1]):
                synonyms[command[1]].append(command[2])
            if command[1] not in synonyms.get(command[2]):
                synonyms[command[2]].append(command[1])
        elif command[0] == 'count':
            if synonyms.get(command[1]) is not None:
                print(len(synonyms[command[1]]))
            else:
                print('0')
        elif command[0] == 'check':
            if command[1] in synonyms.keys() and command[2] in synonyms[command[1]] or \
               command[2] in synonyms.keys() and command[1] in synonyms[command[2]]:
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    syn_func()
