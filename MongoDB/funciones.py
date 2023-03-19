from conexion import conn
from bson.objectid import ObjectId


class Mongo:
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado
    
    def insertar(valor):
        return conn.insert_one({
                "palabra": valor.palabra,
                "significado": valor.significado
            }).inserted_id

    def actualizar(id, valor):
        return conn.update_one(
            {'_id', ObjectId(id)},              
        {'$set':
            {'palabra':valor.palabra, 
                'significado':valor.significado}})
    
    def eliminar(id):
        return conn.delete_one({'_id': ObjectId(id)})
    
    def buscar(id):
        return conn.find_one({'_id': ObjectId(id)}) 
    
    def mostrar():
        data = [slang for slang in conn.find()]
        return f'\n'.join([f'{slang["palabra"]} - {slang["significado"]}' for slang in data])
    
    
    