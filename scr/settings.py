from urllib.parse import quote # por causa do @ na senha...
from dotenv import load_dotenv, find_dotenv
import os
from flask import session
# localiza o arquivo de .env
dotenv_file = find_dotenv()
# Carrega o arquivo .env
load_dotenv(dotenv_file)
# Configurações da API
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")
# Configurações banco de dados
DB_SGDB = os.getenv("DB_SGDB")
DB_NAME = os.getenv("DB_NAME")
# Caso seja diferente de sqlite
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = quote(os.getenv("DB_PASS"))
# Ajusta STR_DATABASE conforme gerenciador escolhido
if DB_SGDB == 'sqlite': # SQLite
    STR_DATABASE = f"sqlite:///{DB_NAME}.db"
elif DB_SGDB == 'mysql': # MySQL
    import pymysql
    STR_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
elif DB_SGDB == 'mssql': # SQL Server
    import pymssql
    STR_DATABASE = f"mssql+pymssql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8"
else: # SQLite
    STR_DATABASE = f"sqlite:///apiDatabase.db"

# Configurações Segurança da API
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

URL_API = os.getenv("URL_API")
# Configuração dos endpoints
ENDPOINT_TOKEN = os.getenv("ENDPOINT_TOKEN")
ENDPOINT_FUNCIONARIO = os.getenv("ENDPOINT_FUNCIONARIO")
ENDPOINT_CLIENTE = os.getenv("ENDPOINT_CLIENTE")
ENDPOINT_PRODUTO = os.getenv("ENDPOINT_PRODUTO")
# Configurações de segurança
def getHeadersAPI():
    return {
        'accept': 'application/json',
        'Authorization': f'Bearer {session["access_token"] if "access_token" in session else ""}'
    }
