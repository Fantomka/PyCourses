syn_dict = {}
for i in range(int(input('number of commands: '))):
    command = (input(f'command {i+1}: ').lower().split())
    if command[0] == 'add':
        syn_dict[command[1]] = command[2]
    elif command[0] == 'count':
        values_dict = list(syn_dict.values())
        print(values_dict.count(command[1]))
    elif command[0] == 'check':
        if command[1] in syn_dict.keys() and syn_dict[command[1]] == command[2] or \
           command[2] in syn_dict.keys() and syn_dict[command[2]] == command[1]:
            print('YES')
        else:
            print('NO')
