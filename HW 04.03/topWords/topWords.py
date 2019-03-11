import bz2
import json
import os
from pprint import pprint
from collections import defaultdict

projectpath = 'C:\\Users\\siman\\Desktop\\курсы\\HW 04.03\\topWords\\'
DirJsonPath = projectpath + 'JsonFolder\\'
DirBz2Path  = projectpath + 'bz2\\'
DirResPath  = projectpath + 'results\\'
json_result = {}

if not os.path.exists(DirJsonPath):
    os.mkdir(DirJsonPath)
    for folder, subfolders, files in os.walk(DirBz2Path):
        for file in files:
            if file.endswith('.bz2'):
                with open(DirBz2Path + file, 'rb') as archive, open(DirJsonPath + file[:-4], 'wb') as output:
                    output.write(bz2.decompress(archive.read()))

for folder, subfolders, files in os.walk(DirJsonPath):
    for file in files:
        with open(DirJsonPath+file, 'r') as json_file:
            for line in json_file.readlines():
                data = json.loads(line)
                if data['body'] not in ['[deleted]', '[removed]']:
                    data = data['body'].lower().split()
                    words = [word.strip(' ,.&;?!<>()[]{}\'"') for word in data if len(word.strip(' ,.&;?!<>()[]{}"\'')) > 2]
                    for word in words:
                        if json_result.get(word) == None:
                            json_result[word] = 1
                        else:
                            json_result[word] = json_result.get(word) + 1

iteration = 0
words_top = {}
for word in sorted(json_result, key=json_result.get, reverse=True):
    if iteration < 20:
        words_top[word] = json_result[word]
        iteration += 1
    else:
        pprint(words_top)
        break
        
if not os.path.exists(DirResPath):
    os.mkdir(DirResPath)
#записать в .\results результаты полного дампа и топа в виде .json
