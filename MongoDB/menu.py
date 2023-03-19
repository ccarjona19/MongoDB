from conexion import client, conn
from funciones import Mongo



while True:
    print('--------------------------------------------------------------')
    print('Este es el menu de nuestra base de datos, ingresa tu accion:\n'
          '1. Agregar valor\n'
          '2. Actualizar valor\n'
          '3. Busca el significado \n'
          '4. Eliminar valor\n'
          '5. Imprimir todos los valores\n'
          '6. Salir')
    
    desicion = input("Que deseas hacer?: ")

    if desicion == '1':
        palabra = input("Ingresa la palabra: ")
        significado = input("Ingresa el significado: ")
        valor = Mongo(palabra, significado)
        id = Mongo.insertar(valor)
        print(f"El id del valor insertado es: {id}\n")
        
    elif desicion == '2':
        id = input("Ingresa el id del valor a actualizar: ")
        palabra = input("Ingresa la palabra: ")
        significado = input("Ingresa el significado: ")
        valor = Mongo(palabra, significado)
        id = Mongo.insertar(valor)
        print("El slang se ha actualizado correctamente\n")
        
    elif desicion == '3':
        id = input("Ingresa el id del valor a buscar: ")
        data = Mongo.buscar(id)
        print(f'El significado de "{data["palabra"]}" es: {data["significado"]}\n')
        
    elif desicion == '4':
        id = input("Ingresa el id del valor a buscar: ")
        Mongo.eliminar(id)
        print("El slang se ha eliminado correctamente\n")
        
    elif desicion == '5':
        print(Mongo.mostrar(),"\n")
            
    elif desicion == '6':
        print("Gracias por usar nuestro programa")
        client.close()
        break
        
        
        
        
    
    

