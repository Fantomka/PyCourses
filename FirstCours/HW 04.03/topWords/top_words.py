r"""
Этот код используется для декомпрессии архивов из папки .\bz2
 и помещает файлы json'a в папку .\JsonFolder для того, чтобы распарсить
 и провести статистику использования слов пользователями reddit
 Результаты приведены в формате .json в папке results
"""

import bz2
import json
import os

JSONPATH = 'JsonFolder'
BZ2PATH = 'bz2'
RESULTPATH = 'results'
JSON_RESULT = {}  # все слова, встречающиеся в файлах json
WORDSTOP = {}  # топ 20 самых встречающихся слов в комментах, взятых из JSON_RESULT


def create_folder(path):
    '''create_folder(path)
    создает папку  по пути path, если path относительная,
    отношение берется от папки где лежит исполняемый модуль
    '''
    if not os.path.exists(path):
        os.mkdir(path)


def decode_bz2(input_archive_path, output_file_path):
    '''decode_bz2(input_archive_path, output_file_path)
    декодирование  архива input_archive_path в output_file_path
    '''
    if file.endswith('.bz2'):
        with open(input_archive_path, 'rb') as archive, open(output_file_path, 'wb') as output:
            output.write(bz2.decompress(archive.read()))


def read_comments_json(file_path, size):
    r'''read_comments_json(file_path, size)

    парсер комментов с reddit'a
    :param file_path: json файл,  который парсим
    :param size: размер слов, которые будет возвращать функция
    :return: словарь
    '''

    words = []
    with open(file_path, 'r') as f_name:
        for line in f_name.readlines():
            buffer = json.loads(line)
            if buffer['body'] not in ['[deleted]', '[removed]']:
                buffer = buffer['body'].lower().split()
                words += [w.strip(' ,.!?;()&') for w in buffer if len(w.strip(' ,.!?;()&')) >= size]
    return words


def top_words(words: dict, n_words: int):
    '''top_words(words: dict, n: int)
    возвращает самые часто используемые слова
    :param words: список слов
    :param n_words: количество возвращаемыx слов
    :return: словарь
    '''
    iteration = 0
    top = {}
    for word in sorted(JSON_RESULT, key=words.get, reverse=True):
        if iteration < n_words:
            top[word] = JSON_RESULT[word]
            iteration += 1
        else:
            break
    return top


create_folder(JSONPATH)
for folder, subfolders, files in os.walk(BZ2PATH):
    for file in files:
        decode_bz2(BZ2PATH + r'/' + file, JSONPATH + r'/' + file[:-4])

for folder, subfolders, files in os.walk(JSONPATH):
    for file in files:
        for Word in read_comments_json(JSONPATH + r'/' + file, 4):
            if JSON_RESULT.get(Word) is None:
                JSON_RESULT[Word] = 1
            else:
                JSON_RESULT[Word] = JSON_RESULT.get(Word) + 1

WORDSTOP = top_words(JSON_RESULT, 20)
create_folder(RESULTPATH)
with open(RESULTPATH + r'/' + 'all_words.json', 'w') as file:
    json.dump(JSON_RESULT, file, indent=4)
with open(RESULTPATH + r'/' + 'top20.json', 'w') as file:
    json.dump(WORDSTOP, file, indent=4)
