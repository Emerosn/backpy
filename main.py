import gzip
import subprocess
from fastapi import FastAPI


app = FastAPI()


# Request return init
@app.get("/")
def root():
    return{"request_success: True"} 


# List files on directory send head param
@app.get("/listfiles/")
def list_files(path: str):
    try:
        output = subprocess.check_output(
                [
                    "ls",
                    "-a",
                    path
                    ]
                ).decode("utf-8") 
        return output.splitlines()
    except Exception as error:
        return str(error)


# Compress  on format gz file 
@app.post("/compress/")
def compress_file(file_path: str):
    try:
        with open(file_path,'rb') as file:
            with gzip.open(file_path+'.gz','wb') as compress_file:
                compress_file.write(file.read())
        compress_file_path = file_path+".gz"
        return compress_file_path
    except Exception  as error:
        return str(error)


# send files with destination being they remote or local
@app.post("/send/")
def send_file(source_path: str,destination_path:str, use_password:bool, use_rsa: bool=False, pass_rsa:str="", password:str = "", port:str = "22"):
    try:
        if use_password:
            if use_rsa:
                output = subprocess.Popen(
                        [
                            "rsync",
                            "-vaurP",
                            "-e",
                            "ssh",
                            "-o",
                            "StrictHostKeyChecking=no",
                            "-I",
                            "{"+pass_rsa+"}",
                            "-p",
                            port,source_path,destination_path
                            ],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                        )
            else:
                output = subprocess.Popen(
                        [
                            "sshpass",
                            "-p",
                            password,
                            "rsync",
                            "-vaurP",
                            "-e",
                            "ssh",
                            "-p",
                            port,
                            source_path,
                            destination_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                        )
        else:
            output = subprocess.Popen(
                [
                    "rsync",
                    "-avz",
                    source_path,
                    destination_path
                    ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
                )
        return output.communicate()[0]

    except Exception as error:
        return str(error)















