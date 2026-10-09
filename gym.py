import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="gimnasio"
)


def registrar_inscripcion():

    nombre_cliente = input("Ingrese el nombre del cliente: ")

    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            break
        except:
            print("Error: debe ingresar un numero")

    print("\n--- TIPO DE MEMBRESIA ---")
    print("1. Basic")
    print("2. Premium")
    print("3. VIP")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if opcion == 1:
        tipo_membresia = "Basic"
        precio_mes = 100
    elif opcion == 2:
        tipo_membresia = "Premium"
        precio_mes = 175
    elif opcion == 3:
        tipo_membresia = "VIP"
        precio_mes = 250
    else:
        print("Opcion invalida")
        return

    while True:
        try:
            meses = int(input("Ingrese la cantidad de meses: "))
            break
        except:
            print("Error: debe ingresar un numero")

    precio_final = precio_mes * meses

    if meses >= 6:
        estado = "ActivePlus"
    else:
        estado = "Active"

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """INSERT INTO inscripciones
        (nombre_cliente, edad, tipo_membresia, meses, precio_final, estado)
        VALUES (%s, %s, %s, %s, %s, %s)"""

        cursor.execute(query, (
            nombre_cliente,
            edad,
            tipo_membresia,
            meses,
            precio_final,
            estado
        ))

        conexion.commit()

        print("La inscripcion se registro correctamente")
        print(f"Su ID es: {cursor.lastrowid}")
        print(f"Precio Final: Q{precio_final}")
        print(f"Estado: {estado}")

        cursor.close()


def consultar_inscripciones():

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "SELECT * FROM inscripciones"

        cursor.execute(query)

        resultados = cursor.fetchall()

        print("\n--- INSCRIPCIONES REGISTRADAS ---")

        for inscripcion in resultados:

            print("-----------------------------")
            print("ID:", inscripcion[0])
            print("Cliente:", inscripcion[1])
            print("Edad:", inscripcion[2])
            print("Tipo de membresia:", inscripcion[3])
            print("Meses contratados:", inscripcion[4])
            print("Precio Final: Q" + str(inscripcion[5]))
            print("Estado:", inscripcion[6])

        cursor.close()


def actualizar_inscripcion():

    while True:
        try:
            id_inscripcion = int(input("Ingrese el ID de la inscripcion que desea actualizar: "))
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

    print("\n--- TIPO DE MEMBRESIA ---")
    print("1. Basic")
    print("2. Premium")
    print("3. VIP")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if opcion == 1:
        tipo_membresia = "Basic"
        precio_mes = 100
    elif opcion == 2:
        tipo_membresia = "Premium"
        precio_mes = 175
    elif opcion == 3:
        tipo_membresia = "VIP"
        precio_mes = 250
    else:
        print("Opcion invalida")
        return

    while True:
        try:
            meses = int(input("Ingrese la nueva cantidad de meses: "))
            break
        except:
            print("Error: debe ingresar un numero")

    precio_final = precio_mes * meses

    if meses >= 6:
        estado = "ActivePlus"
    else:
        estado = "Active"

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """UPDATE inscripciones
        SET nombre_cliente=%s,
        edad=%s,
        tipo_membresia=%s,
        meses=%s,
        precio_final=%s,
        estado=%s
        WHERE id=%s"""

        cursor.execute(query, (
            nombre_cliente,
            edad,
            tipo_membresia,
            meses,
            precio_final,
            estado,
            id_inscripcion
        ))

        conexion.commit()

        print("La inscripcion se actualizo correctamente")
        print(f"Nuevo Precio Final: Q{precio_final}")
        print(f"Nuevo Estado: {estado}")

        cursor.close()


def eliminar_inscripcion():

    while True:
        try:
            id_inscripcion = int(input("Ingrese el ID de la inscripcion para borrar: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "DELETE FROM inscripciones WHERE id = %s"

        cursor.execute(query, (id_inscripcion,))

        conexion.commit()

        print("LA INSCRIPCION SE BORRO EXITOSAMENTE")

        cursor.close()


def menu():

    print("\n--- MENU PRINCIPAL ---")
    print("1. Registrar inscripcion")
    print("2. Consultar inscripciones")
    print("3. Actualizar inscripcion")
    print("4. Eliminar inscripcion")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    match opcion:

        case 1:
            registrar_inscripcion()
            menu()

        case 2:
            consultar_inscripciones()
            menu()

        case 3:
            actualizar_inscripcion()
            menu()

        case 4:
            eliminar_inscripcion()
            menu()

        case 5:
            print("Saliendo del programa...")

            if conexion.is_connected():
                conexion.close()

        case _:
            print("Ingrese un dato valido")
            menu()


menu()