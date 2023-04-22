import gzip
import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    print("Resquest Sucessfuk")
    return 200


@app.post("/compress")
def compress_file(path: str):
    with open(path,'rb') as list_files:
        with gzip.open(path+'.gz','wb') as list_comprimido:
            list_comprimido.write(list_files.read())
    return path + ".gz"

