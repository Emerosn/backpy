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
        output = subprocess.check_output(
                [
                    "ls",
                    "-a",
                    path
                    ]
                ).decode("utf-8") 
        return output.splitlines()
    except Exception as e:
        return e


# Compress  on format gz file 
@app.post("/compress/")
def compress_file(t,path: str):
    try:
        with open(path,'rb') as list_files:
            with gzip.open(path+'.gz','wb') as list_comprimido:
                list_comprimido.write(list_files.read())
        output=path+".gz"
        return output
    except Exception  as e:
        return e


@app.post("/send/")
def send_file(pathin: str,pathout: str,use_password:bool,password:str = ""):
    try:
        if use_password:
            with temp_password_file(mode=w, delete=False) as password_file:
                password_file.write(password)
            output =subprocess.Popen(
                    [
                        "rsync",
                        "-avz",
                        "--password-file",
                        password_file,
                        pathin,
                        pathout
                        ],
                    stdout=subprocess.PIPE
                    )
        else:
            output =subprocess.Popen(
                [
                    "rsync",
                    "-avz",
                    pathin,
                    pathout
                    ],
                stdout=subprocess.PIPE
                )
        return output.communicate()[0]

    except Exception as e:
        return str(e)















