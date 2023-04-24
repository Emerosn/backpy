# API de Compressão de Arquivos

Esta é uma API simples construída em Python com a biblioteca FastAPI para compressão de arquivos usando o algoritmo gzip.
## Variaveis

<p>GET "/listfiles/"
Parâmetros:
- path (str): o caminho para o diretório a ser listado.

Retorna uma lista dos nomes dos arquivos e diretórios no diretório especificado por `path`. Se ocorrer um erro, uma string contendo a mensagem de erro será retornada.
<p/>
<p>
POST "/compress/"
Parâmetros:
- file_path (str): o caminho completo para o arquivo que será comprimido.

Comprime o arquivo especificado por `file_path` usando o formato gzip e retorna o caminho completo para o arquivo comprimido. Se ocorrer um erro, uma string contendo a mensagem de erro será retornada.
<p/>
<p>
POST "/send/"
Parâmetros:
- source_path (str): o caminho completo para o arquivo ou diretório que será enviado.
- destination_path (str): o caminho completo para o destino do envio.
- use_password (bool): indica se deve ser usada uma senha para autenticação no destino. Se for True, deve-se fornecer o parâmetro `password`.
- password (str, opcional): a senha para autenticação no destino. Requer `use_password=True`.

Envia o arquivo ou diretório especificado por `source_path` para o destino especificado por `destination_path`. Se `use_password` for True, o parâmetro `password` deve ser fornecido e uma senha temporária será criada em disco para uso no processo de envio. Retorna a saída do processo de envio. Se ocorrer um erro, uma string contendo a mensagem de erro será retornada.
<p/>

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
