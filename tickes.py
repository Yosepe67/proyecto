import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="concierto"
)


def agregar():

    nombre = input("INGRESE EL NOMBRE: ")
    apellido = input("INGRESE EL APELLIDO: ")
    personas = int(input("INGRESE EL NUMERO DE PERSONAS: "))

    print("1. NORMAL")
    print("2. VIP")
    print("3. DIAMANTE")

    opcion = int(input("INGRESE EL TIPO DE TICKET: "))

    if opcion == 1:
        tipo = "Normal"

    elif opcion == 2:
        tipo = "VIP"

    elif opcion == 3:
        tipo = "Diamante"

    else:
        print("OPCION NO VALIDA")
        menu()
        return

    cursor = conexion.cursor()

    query = """INSERT INTO tickets
    (firstName, lastName, numberOfPeople, ticketType)
    VALUES (%s, %s, %s, %s)"""

    cursor.execute(query, (nombre, apellido, personas, tipo))

    conexion.commit()

    print("TICKET AGREGADO CORRECTAMENTE")

    cursor.close()

    menu()


def consultar():

    cursor = conexion.cursor()

    query = "SELECT * FROM tickets"

    cursor.execute(query)

    datos = cursor.fetchall()

    print("\n--- TICKETS REGISTRADOS ---")

    if len(datos) == 0:

        print("NO HAY TICKETS REGISTRADOS")

    else:

        for ticket in datos:

            print("----------------------------")
            print("ID:", ticket[0])
            print("NOMBRE:", ticket[1])
            print("APELLIDO:", ticket[2])
            print("NUMERO DE PERSONAS:", ticket[3])
            print("TIPO DE TICKET:", ticket[4])

    cursor.close()

    menu()


def actualizar():

    id = int(input("INGRESE EL ID PARA ACTUALIZAR: "))

    nombre = input("INGRESE EL NUEVO NOMBRE: ")
    apellido = input("INGRESE EL NUEVO APELLIDO: ")
    personas = int(input("INGRESE EL NUEVO NUMERO DE PERSONAS: "))

    print("1. NORMAL")
    print("2. VIP")
    print("3. DIAMANTE")

    opcion = int(input("INGRESE EL TIPO DE TICKET: "))

    if opcion == 1:
        tipo = "Normal"

    elif opcion == 2:
        tipo = "VIP"

    elif opcion == 3:
        tipo = "Diamante"

    else:
        print("OPCION NO VALIDA")
        menu()
        return

    cursor = conexion.cursor()

    query = """UPDATE tickets
    SET firstName=%s,
    lastName=%s,
    numberOfPeople=%s,
    ticketType=%s
    WHERE id=%s"""

    cursor.execute(query, (nombre, apellido, personas, tipo, id))

    conexion.commit()

    print("TICKET ACTUALIZADO CORRECTAMENTE")

    cursor.close()

    menu()


def eliminar():

    id = int(input("INGRESE EL ID PARA ELIMINAR: "))

    cursor = conexion.cursor()

    query = "DELETE FROM tickets WHERE id=%s"

    cursor.execute(query, (id,))

    conexion.commit()

    print("TICKET ELIMINADO CORRECTAMENTE")

    cursor.close()

    menu()


def menu():

    print("\n--- SISTEMA DE TICKETS ---")
    print("1. AGREGAR")
    print("2. CONSULTAR")
    print("3. ACTUALIZAR")
    print("4. ELIMINAR")
    print("5. SALIR")

    opcion = int(input("INGRESE LA OPCION: "))

    if opcion == 1:

        agregar()

    elif opcion == 2:

        consultar()

    elif opcion == 3:

        actualizar()

    elif opcion == 4:

        eliminar()

    elif opcion == 5:

        print("PROGRAMA FINALIZADO")
        conexion.close()

    else:

        print("OPCION NO VALIDA")
        menu()


menu()