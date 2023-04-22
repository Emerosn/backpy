import gzip
import subprocess
from fastapi import FastAPI


app = FastAPI()


# Request return init
@app.get("/")
def root():
    return{"request: True"} 


# List files on directory send head param
@app.get("/listfiles/")
def get_list(path: str):
    try:
        output = subprocess.check_output(["ls","-a",path]).decode("utf-8") 
        print(output.splitlines())
    except Exception as e:
        print(e)
    return {"files":output.splitlines()}


# Compress  on format gz file 
@app.post("/compress/")
def compress_file(path: str):
    try:
        with open(path,'rb') as list_files:
            with gzip.open(path+'.gz','wb') as list_comprimido:
                list_comprimido.write(list_files.read())
    except Exception  as e:
        print(e)
    return path + ".gz"


# Send backup for one local directory or remote directory

