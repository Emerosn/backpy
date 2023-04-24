# API de Compressão de Arquivos

This is a simple API built in Python with the FastAPI library for file compression using the gzip algorithm.
Endpoints

GET "/listfiles/"

Parameters:

    path (str): the path to the directory to be listed.

Returns a list of file and directory names in the directory specified by path. If an error occurs, a string containing the error message will be returned.

POST "/compress/"

Parameters:

    file_path (str): the full path to the file to be compressed.

Compresses the file specified by file_path using the gzip format and returns the full path to the compressed file. If an error occurs, a string containing the error message will be returned.

POST "/send/"

Parameters:

    source_path (str): the full path to the file or directory to be sent.
    destination_path (str): the full path to the destination of the send.
    use_password (bool): indicates whether a password should be used for authentication at the destination. If True, the password parameter must be provided.
    password (str, optional): the password for authentication at the destination. Requires use_password=True.

Sends the file or directory specified by source_path to the destination specified by destination_path. If use_password is True, the password parameter must be provided, and a temporary password file will be created on disk for use in the send process. Returns the output of the send process. If an error occurs, a string containing the error message will be returned.

# Installation

To use this API, you'll need to have Python 3.7 or higher installed on your system. You may also need to install the FastAPI and gzip libraries using the following command:

```
pip install fastapi gzip
```

Usage

To start the API, run the following command in a terminal:

```
uvicorn main:app --reload
```

This will start the server, and the API will be ready to use.
Compressing a File

To compress a file, make an HTTP POST request to the /compress route, passing the file path as a parameter in the request body. For example:

```
curl -X POST -d '{"path": "/path/to/file.txt"}' http://localhost:8000/compress
```

This will compress the file /path/to/file.txt using gzip and return the path to the compressed file (/path/to/file.txt.gz).
