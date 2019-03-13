'''
Этот модуль реализует словарь синонимов с командами:
add word1 word2
count word
check word1 word2
'''

Synonyms = {}
for i in range(int(input('number of commands: '))):
    command = input(f'command {i+1}: ').lower().split()
    if command[0] == 'add':
        if Synonyms.get(command[1]) is None:
            Synonyms[command[1]] = []
        if Synonyms.get(command[2]) is None:
            Synonyms[command[2]] = []
        if command[2] not in Synonyms.get(command[1]):
            Synonyms[command[1]].append(command[2])
        if command[1] not in Synonyms.get(command[2]):
            Synonyms[command[2]].append(command[1])
        print(Synonyms)
    elif command[0] == 'count':
        if Synonyms.get(command[1]) is not None:
            print(len(Synonyms[command[1]]))
        else:
            print('0')
    elif command[0] == 'check':
        if command[1] in Synonyms.keys() and command[2] in Synonyms[command[1]] or \
           command[2] in Synonyms.keys() and command[1] in Synonyms[command[2]]:
            print('YES')
        else:
            print('NO')
