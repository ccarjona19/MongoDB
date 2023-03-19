from conexion import conn


diccionario = [{"palabra": "tongo", "significado": "policia"},
        {"palabra": "gringo", "significado": "persona de origen anglo no habla espaniol"},
        {"palabra": "mopri", "significado": "primo"},
        {"palabra": "llesca", "significado": "calle"},
        {"palabra": "compa", "significado": "compadre"}]


data = conn.distinct('palabra')
slangs = [slang for slang in diccionario if slang['palabra'] not in data]

if slangs:
    res = conn.insert_many(slangs)