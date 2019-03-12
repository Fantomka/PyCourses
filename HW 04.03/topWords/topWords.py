import bz2
import json
import os

projectpath = 'C:\\Users\\siman\\Desktop\\курсы\\HW 04.03\\topWords\\'
DirJsonPath = projectpath + 'JsonFolder\\'
DirBz2Path  = projectpath + 'bz2\\'
DirResPath  = projectpath + 'results\\'
json_result = {}  # все слова, встречающиеся в файлах json
words_top = {}  # топ 20 самых встречающихся слов в комментах, взятых из json_result


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def decode_bz2(input_file_path, output_file_path):
    if file.endswith('.bz2'):
        with open(input_file_path, 'rb') as archive, open(output_file_path, 'wb') as output:
            output.write(bz2.decompress(archive.read()))


def read_comments_json(file_path, size):
    words = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            json_dict = json.loads(line)
            if json_dict['body'] not in ['[deleted]', '[removed]']:
                json_dict = json_dict['body'].lower().split()
                words += [w.strip(' ,.&;?!<>()[]{}\'"') for w in json_dict if len(w.strip(' ,.&;?!<>()[]{}"\'')) >= size]
    return words


def top_words(words, n):
    iter = 0
    top = {}
    for word in sorted(json_result, key=words.get, reverse=True):
        if iter < n:
            top[word] = json_result[word]
            iter += 1
        else:
            return top


create_folder(DirJsonPath)
for folder, subfolders, files in os.walk(DirBz2Path):
    break
for file in files:
    decode_bz2(DirBz2Path+file, DirJsonPath + file[:-4])

for folder, subfolders, files in os.walk(DirJsonPath):
    break
for file in files:
    for word in read_comments_json(DirJsonPath+file, 4):
        if json_result.get(word) == None:
            json_result[word] = 1
        else:
            json_result[word] = json_result.get(word) + 1

words_top = top_words(json_result, 20)
create_folder(DirResPath)
with open(DirResPath + 'all_words.json', 'w') as file:
    json.dump(json_result, file, indent = 4)
with open(DirResPath + 'top20.json', 'w') as file:
    json.dump(words_top, file, indent = 4)
