import subprocess
import gzip
import shutil

path = input("Caminho do arquivo: ")

with open(path,'rb') as list_files:
    with gzip.open(path+'.gz','wb') as list_comprimido:
        list_comprimido.write(list_files.read())