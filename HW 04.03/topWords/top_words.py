r"""
Этот код используется для декомпрессии архивов из папки .\bz2
 и помещает файлы json'a в папку .\JsonFolder для того, чтобы распарсить
 и провести статистику использования слов пользователями reddit
 Результаты приведены в формате .json в папке results

"""

import bz2
import json
import os

JSONPath = 'JsonFolder\\'
BZ2Path = 'bz2\\'
ResultsPath = 'results\\'
json_result = {}  # все слова, встречающиеся в файлах json
WordsTop = {}  # топ 20 самых встречающихся слов в комментах, взятых из json_result


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
                words += [w.strip(' ,.!?;') for w in buffer if len(w.strip(' ,.;?!')) >= size]
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
    for word in sorted(json_result, key=words.get, reverse=True):
        if iteration < n_words:
            top[word] = json_result[word]
            iteration += 1
        else:
            break
    return top


create_folder(JSONPath)
for folder, subfolders, files in os.walk(BZ2Path):
    for file in files:
        decode_bz2(BZ2Path+file, JSONPath + file[:-4])

for folder, subfolders, files in os.walk(JSONPath):
    for file in files:
        for Word in read_comments_json(JSONPath+file, 4):
            if json_result.get(Word) is None:
                json_result[Word] = 1
            else:
                json_result[Word] = json_result.get(Word) + 1

WordsTop = top_words(json_result, 20)
create_folder(ResultsPath)
with open(ResultsPath + 'all_words.json', 'w') as file:
    json.dump(json_result, file, indent=4)
with open(ResultsPath + 'top20.json', 'w') as file:
    json.dump(WordsTop, file, indent=4)
