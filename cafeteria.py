import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cafeteria"
)


def registrar_pedido():

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    nombre_producto = input("Ingrese el nombre del producto: ")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except:
            print("Error: debe ingresar un numero")

    print("\n--- TIPO DE CLIENTE ---")
    print("1. Regular")
    print("2. Student")
    print("3. Teacher")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if opcion == 1:
        tipo_pedido = "Regular"
        descuento = 0
    elif opcion == 2:
        tipo_pedido = "Student"
        descuento = 10
    elif opcion == 3:
        tipo_pedido = "Teacher"
        descuento = 15
    else:
        print("Opcion invalida")
        return

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """INSERT INTO pedidos
        (nombre_cliente, nombre_producto, cantidad, tipo_pedido, descuento)
        VALUES (%s, %s, %s, %s, %s)"""

        cursor.execute(query, (
            nombre_cliente,
            nombre_producto,
            cantidad,
            tipo_pedido,
            descuento
        ))

        conexion.commit()

        print("El pedido se registro correctamente")
        print(f"Su ID es: {cursor.lastrowid}")

        cursor.close()


def consultar_pedidos():

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "SELECT * FROM pedidos"

        cursor.execute(query)

        resultados = cursor.fetchall()

        print("\n--- PEDIDOS REGISTRADOS ---")

        for pedido in resultados:

            print("-----------------------------")
            print("ID:", pedido[0])
            print("Cliente:", pedido[1])
            print("Producto:", pedido[2])
            print("Cantidad:", pedido[3])
            print("Tipo de cliente:", pedido[4])
            print("Descuento:", pedido[5])

        cursor.close()


def actualizar_pedido():

    while True:
        try:
            id_pedido = int(input("Ingrese el ID del pedido que desea actualizar: "))
            break
        except:
            print("Error: debe ingresar un numero")

    nombre_cliente = input("Ingrese el nuevo nombre del cliente: ")
    nombre_producto = input("Ingrese el nuevo nombre del producto: ")

    while True:
        try:
            cantidad = int(input("Ingrese la nueva cantidad: "))
            break
        except:
            print("Error: debe ingresar un numero")

    print("\n--- TIPO DE CLIENTE ---")
    print("1. Regular")
    print("2. Student")
    print("3. Teacher")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if opcion == 1:
        tipo_pedido = "Regular"
        descuento = 0
    elif opcion == 2:
        tipo_pedido = "Student"
        descuento = 10
    elif opcion == 3:
        tipo_pedido = "Teacher"
        descuento = 15
    else:
        print("Opcion invalida")
        return

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """UPDATE pedidos
        SET nombre_cliente=%s,
        nombre_producto=%s,
        cantidad=%s,
        tipo_pedido=%s,
        descuento=%s
        WHERE idpedidos=%s"""

        cursor.execute(query, (
            nombre_cliente,
            nombre_producto,
            cantidad,
            tipo_pedido,
            descuento,
            id_pedido
        ))

        conexion.commit()

        print("El pedido se actualizo correctamente")

        cursor.close()


def eliminar_pedido():

    while True:
        try:
            id_pedido = int(input("Ingrese el ID del pedido para borrar: "))
            break
        except:
            print("Error: debe ingresar un numero")

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "DELETE FROM pedidos WHERE idpedidos = %s"

        cursor.execute(query, (id_pedido,))

        conexion.commit()

        print("EL PEDIDO SE BORRO EXITOSAMENTE")

        cursor.close()


def menu():

    print("\n--- MENU PRINCIPAL ---")
    print("1. Registrar pedido")
    print("2. Consultar pedidos")
    print("3. Actualizar pedido")
    print("4. Eliminar pedido")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            break
        except:
            print("Error: debe ingresar un numero")

    match opcion:

        case 1:
            registrar_pedido()

        case 2:
            consultar_pedidos()

        case 3:
            actualizar_pedido()

        case 4:
            eliminar_pedido()

        case 5:
            print("Saliendo del programa...")

            if conexion.is_connected():
                conexion.close()

        case _:
            print("Ingrese un dato valido")


menu()