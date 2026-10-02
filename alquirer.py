import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="alquileres"
)


def registrar_alquiler():

    nombre_cliente = input("Ingrese el nombre del cliente: ")

    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            break
        except:
            print("Error: debe ingresar un numero")

    print("\n--- TIPO DE VEHICULO ---")
    print("1. Car")
    print("2. Motorcycle")
    print("3. SUV")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if opcion == 1:
        tipo_de_vehiculo = "Car"
        precio_dia = 200
    elif opcion == 2:
        tipo_de_vehiculo = "Motorcycle"
        precio_dia = 100
    elif opcion == 3:
        tipo_de_vehiculo = "SUV"
        precio_dia = 350
    else:
        print("Opcion invalida")
        return

    while True:
        try:
            dias_renta = int(input("Ingrese los dias de renta: "))
            break
        except:
            print("Error: debe ingresar un numero")

    precio_final = precio_dia * dias_renta

    if dias_renta >= 5:
        estado = "RentaLarga"
    else:
        estado = "RentaCorta"

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """INSERT INTO alquileres
        (nombre_cliente, edad, tipo_de_vehiculo, dias_renta, precio_final, estado)
        VALUES (%s, %s, %s, %s, %s, %s)"""

        cursor.execute(query, (
            nombre_cliente,
            edad,
            tipo_de_vehiculo,
            dias_renta,
            precio_final,
            estado
        ))

        conexion.commit()

        print("El alquiler se registro correctamente")
        print(f"Su ID es: {cursor.lastrowid}")
        print(f"Precio Final: Q{precio_final}")
        print(f"Estado: {estado}")

        cursor.close()


def consultar_alquileres():

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "SELECT * FROM alquileres"

        cursor.execute(query)

        resultados = cursor.fetchall()

        print("\n--- ALQUILERES REGISTRADOS ---")

        for alquiler in resultados:

            print("-----------------------------")
            print("ID:", alquiler[0])
            print("Cliente:", alquiler[1])
            print("Edad:", alquiler[2])
            print("Tipo de vehiculo:", alquiler[3])
            print("Dias de renta:", alquiler[4])
            print("Precio Final: Q" + str(alquiler[5]))
            print("Estado:", alquiler[6])

        cursor.close()


def actualizar_alquiler():

    while True:
        try:
            id_alquiler = int(input("Ingrese el ID del alquiler que desea actualizar: "))
            break
        except:
            print("Error: debe ingresar un numero")

    nombre_cliente = input("Ingrese el nuevo nombre del cliente: ")

    while True:
        try:
            edad = int(input("Ingrese la nueva edad: "))
            break
        except:
            print("Error: debe ingresar un numero")

    print("\n--- TIPO DE VEHICULO ---")
    print("1. Car")
    print("2. Motorcycle")
    print("3. SUV")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if opcion == 1:
        tipo_de_vehiculo = "Car"
        precio_dia = 200
    elif opcion == 2:
        tipo_de_vehiculo = "Motorcycle"
        precio_dia = 100
    elif opcion == 3:
        tipo_de_vehiculo = "SUV"
        precio_dia = 350
    else:
        print("Opcion invalida")
        return

    while True:
        try:
            dias_renta = int(input("Ingrese los nuevos dias de renta: "))
            break
        except:
            print("Error: debe ingresar un numero")

    precio_final = precio_dia * dias_renta

    if dias_renta >= 5:
        estado = "LongRental"
    else:
        estado = "ShortRental"

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """UPDATE alquileres
        SET nombre_cliente=%s,
        edad=%s,
        tipo_de_vehiculo=%s,
        dias_renta=%s,
        precio_final=%s,
        estado=%s
        WHERE idalquileres=%s"""

        cursor.execute(query, (
            nombre_cliente,
            edad,
            tipo_de_vehiculo,
            dias_renta,
            precio_final,
            estado,
            id_alquiler
        ))

        conexion.commit()

        print("El alquiler se actualizo correctamente")
        print(f"Nuevo Precio Final: Q{precio_final}")
        print(f"Nuevo Estado: {estado}")

        cursor.close()


def eliminar_alquiler():

    while True:
        try:
            id_alquiler = int(input("Ingrese el ID del alquiler para borrar: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "DELETE FROM alquileres WHERE idalquileres = %s"

        cursor.execute(query, (id_alquiler,))

        conexion.commit()

        print("EL ALQUILER SE BORRO EXITOSAMENTE")

        cursor.close()


def menu():

    print("\n--- MENU PRINCIPAL ---")
    print("1. Registrar alquiler")
    print("2. Consultar alquileres")
    print("3. Actualizar alquiler")
    print("4. Eliminar alquiler")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    match opcion:

        case 1:
            registrar_alquiler()
            menu()

        case 2:
            consultar_alquileres()
            menu()

        case 3:
            actualizar_alquiler()
            menu()

        case 4:
            eliminar_alquiler()
            menu()

        case 5:
            print("Saliendo del programa...")

            if conexion.is_connected():
                conexion.close()

        case _:
            print("Ingrese un dato valido")
            menu()


menu()