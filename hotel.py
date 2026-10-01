import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="reservas_hotel"
)


def registrar_cita():

    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    while True:
        try:
            numero_huespedes = int(input("Ingrese el numero de huespedes: "))
            break
        except:
            print("Error: debe ingresar un numero")

    print("\n--- TIPOS DE HABITACION ---")
    print("1. Standard")
    print("2. Deluxe")
    print("3. Suite")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if opcion == 1:
        tipo_habitacion = "Standard"
    elif opcion == 2:
        tipo_habitacion = "Deluxe"
    elif opcion == 3:
        tipo_habitacion = "Suite"
    else:
        print("Opcion invalida")
        return

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """INSERT INTO citas
        (nombre, apellido, numero_huespedes, tipo_habitacion)
        VALUES (%s, %s, %s, %s)"""

        cursor.execute(query, (
            nombre,
            apellido,
            numero_huespedes,
            tipo_habitacion
        ))

        conexion.commit()

        print("La reserva se registro correctamente")
        print(f"Su ID es: {cursor.lastrowid}")

        cursor.close()


def consultar_citas():

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "SELECT * FROM citas"

        cursor.execute(query)

        resultados = cursor.fetchall()

        print("\n--- RESERVAS REGISTRADAS ---")

        for cita in resultados:

            print("-----------------------------")
            print("ID:", cita[0])
            print("Nombre:", cita[1])
            print("Apellido:", cita[2])
            print("Numero de huespedes:", cita[3])
            print("Tipo de habitacion:", cita[4])

        cursor.close()


def actualizar_cita():

    while True:
        try:
            id_cita = int(input("Ingrese el ID de la reserva que desea actualizar: "))
            break
        except:
            print("Error: debe ingresar un numero")

    nombre = input("Ingrese el nuevo nombre: ")
    apellido = input("Ingrese el nuevo apellido: ")

    while True:
        try:
            numero_huespedes = int(input("Ingrese el nuevo numero de huespedes: "))
            break
        except:
            print("Error: debe ingresar un numero")

    print("\n--- TIPOS DE HABITACION ---")
    print("1. Standard")
    print("2. Deluxe")
    print("3. Suite")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if opcion == 1:
        tipo_habitacion = "Standard"
    elif opcion == 2:
        tipo_habitacion = "Deluxe"
    elif opcion == 3:
        tipo_habitacion = "Suite"
    else:
        print("Opcion invalida")
        return

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """UPDATE citas
        SET nombre=%s,
        apellido=%s,
        numero_huespedes=%s,
        tipo_habitacion=%s
        WHERE id=%s"""

        cursor.execute(query, (
            nombre,
            apellido,
            numero_huespedes,
            tipo_habitacion,
            id_cita
        ))

        conexion.commit()

        print("La reserva se actualizo correctamente")

        cursor.close()


def eliminar_cita():

    while True:
        try:
            id_cita = int(input("Ingrese el ID de la reserva para borrar: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "DELETE FROM citas WHERE id = %s"

        cursor.execute(query, (id_cita,))

        conexion.commit()

        print("LA RESERVA SE BORRO EXITOSAMENTE")

        cursor.close()


def menu():

    while True:

        print("\n--- MENU PRINCIPAL ---")
        print("1. Registrar reserva")
        print("2. Consultar reservas")
        print("3. Actualizar reserva")
        print("4. Eliminar reserva")
        print("5. Salir")

        try:
            desi = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")


    match desi:

        case 1:
            registrar_cita()

        case 2:
            consultar_citas()

        case 3:
            actualizar_cita()

        case 4:
            eliminar_cita()

        case 5:
            print("Saliendo del programa...")

            if conexion.is_connected():
                conexion.close()

        case _:
            print("Ingrese un dato valido")


menu()