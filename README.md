# backpy


# API de Compressão de Arquivos

Esta é uma API simples construída em Python com a biblioteca FastAPI para compressão de arquivos usando o algoritmo gzip.

## Instalação

Para usar esta API, você precisará ter o Python 3.7 ou superior instalado em seu sistema. Você também pode precisar instalar a biblioteca FastAPI e o gzip, usando o seguinte comando:

```bash
pip install -r requirements.txt

```

Para iniciar a API, execute o seguinte comando em um terminal:

bash

uvicorn main:app --reload

Isso iniciará o servidor e a API estará pronta para ser usada.
Compressão de arquivo

Para comprimir um arquivo, faça uma solicitação HTTP POST para a rota /compress, passando o caminho do arquivo como parâmetro no corpo da solicitação. Por exemplo:

bash

curl -X POST -d '{"path": "/caminho/do/arquivo.txt"}' http://localhost:8000/compress

Isso comprimirá o arquivo /caminho/do/arquivo.txt usando gzip e retornará o caminho do arquivo comprimido (/caminho/do/arquivo.txt.gz).
Teste da raiz

Para testar a raiz da API, faça uma solicitação HTTP GET para a rota /. Isso imprimirá a mensagem "Request Successful" no console e retornará o código de status 200.
Licença

Este projeto está sob a licença MIT. Leia o arquivo LICENSE para obter mais informações.

less


Este texto formatado em Markdown será exibido como segue:

# API de Compressão de Arquivos

Esta é uma API simples construída em Python com a biblioteca FastAPI para compressão de arquivos usando o algoritmo gzip.

## Instalação

Para usar esta API, você precisará ter o Python 3.7 ou superior instalado em seu sistema. Você também pode precisar instalar a biblioteca FastAPI e o gzip, usando o seguinte comando:

```
pip install fastapi gzip
```
Uso

Para iniciar a API, execute o seguinte comando em um terminal:


```
uvicorn main:app --reload
```
Isso iniciará o servidor e a API estará pronta para ser usada.
Compressão de arquivo

Para comprimir um arquivo, faça uma solicitação HTTP POST para a rota /compress, passando o caminho do arquivo como parâmetro no corpo da solicitação. Por exemplo:

```
curl -X POST -d '{"path": "/caminho/do/arquivo.txt"}' http://localhost:8000/compress
```
Isso comprimirá o arquivo /caminho/do/arquivo.txt usando gzip e retornará o caminho do arquivo comprimido (/caminho/do/arquivo.txt.gz).
Teste da raiz

Para testar a raiz da API, faça uma solicitação HTTP GET para a rota /. Isso imprimirá a mensagem "Request Successful" no console e retornará o código de status 200.

#### Este projeto está sob a licença MIT. Leia o arquivo LICENSE para obter mais informações.