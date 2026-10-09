import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ProjecIF"
)
def delete():
    id = int(input("INGRESE EL ID PARA ELIMINAR:"))
    if conexion.is_connected():
         cursor = conexion.cursor
         Query = "DELETE FROM Ejercicie"


def agregar():
     name = input("INGRESE SU NOMBRE:")
     Est = int(input("1.ACT",)("2.INA"))
     estado = "Activo"if Est == 1 else "inactivo"

     if conexion.is_connected():
         
      cursor = conexion.cursor()
     
     query = """INSERT INTO informacion
        (name,Est,estado,)
        VALUES (%s, %s, %s,)"""




def menu():
    print ("WELCOM TO THE PROGAM OF THE NAME YOSEPE")
    lista = ["1 AGREGAR""2.ELEMINAR"]
    for lista in lista
    print(lista)


    desi = int(input("INGRESE LA SIGUIENTE OPCION"))

    if desi == 1:
        pass
    elif desi == 2:
        pass
    else
        
        