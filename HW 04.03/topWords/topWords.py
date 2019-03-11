import bz2
import json
import os

projectpath = 'C:\\Users\\siman\\Desktop\\topWords\\'
DirJsonPath = projectpath + 'JsonFolder\\'
DirBz2Path  = projectpath + 'bz2\\'

if not os.path.exists(DirJsonPath):
    os.mkdir(DirJsonPath)
    for folder, subfolders, files in os.walk(DirBz2Path):
        for file in files:
            if file.endswith('.bz2'):
                with open(DirBz2Path + file, 'rb') as archive, open(DirJsonPath + file[:-4], 'wb') as output:
                    output.write(bz2.decompress(archive.read()))
                output.close()
                archive.close()





