'''
Created on 10 mar 2025

@author: Iri
'''
import mysql.connector



def conectar():
    conexion=mysql.connector.connect(#establece la conexión
        host="localhost",
        user="root",
        password="",
        database="gestioncitas"
    )
    return conexion



def insertar(nombre,apellido,telefono,fecha):
    print("La función sí se ejecuta")
    conexion=conectar()
    if conexion is None:
        print("No se está conectando a la base de datos")
        return
    cursor=conexion.cursor()
    query="INSERT INTO citas (nombre, apellido, telefono, fecha_cita) VALUES (%s, %s, %s, %s)"
    valores=(nombre, apellido,telefono,fecha)
    cursor.execute(query, valores)
    conexion.commit()
    print("La cita ha sido añadida a la base de datos")
    print(f"{nombre} {apellido} - {fecha}")
    cursor.close()
    conexion.close()
    
    
 
#if conexion.is_connected():
 #   print("La conexión se produjo")
  #  conexion.close()
#else:
 #   print("No se está conectando a la base de datos")