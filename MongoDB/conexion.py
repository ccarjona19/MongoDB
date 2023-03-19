from pymongo import MongoClient


conn = MongoClient()

MONGO_HOST = '127.0.0.1'
MONGO_PORT = '27017'
MONGO_TIMEOUT = 1000

CONEXION = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"


try:
    client = MongoClient(CONEXION, serverSelectionTimeoutMS=MONGO_TIMEOUT)
    print(f'------ Conexion realizada ------ {MONGO_HOST}\n')
    colecction = client['mongo_slangs']
    conn = colecction['Slags']
    
except Exception:
    print(f'----- Error ------')