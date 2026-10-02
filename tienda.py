import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pipi_shop"
)


def registrar_producto():

    nombre_producto = input("Ingrese el nombre del producto: ")

    print("\n--- CATEGORIA ---")
    print("1. Technology")
    print("2. Food")
    print("3. Clothing")

    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        categoria = "Technology"
    elif opcion == 2:
        categoria = "Food"
    elif opcion == 3:
        categoria = "Clothing"
    else:
        print("Opcion invalida")
        return

    stock = int(input("Ingrese el stock: "))
    precio = float(input("Ingrese el precio: "))
    proveedor = input("Ingrese el proveedor: ")

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """INSERT INTO productos
        (nombre_producto, categoria, stock, precio, proveedor)
        VALUES (%s, %s, %s, %s, %s)"""

        cursor.execute(query, (
            nombre_producto,
            categoria,
            stock,
            precio,
            proveedor
        ))

        conexion.commit()

        print("El producto se registro correctamente")
        print("Su ID es:", cursor.lastrowid)

        cursor.close()


def consultar_productos():

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "SELECT * FROM productos"

        cursor.execute(query)

        resultados = cursor.fetchall()

        print("\n--- INVENTARIO ---")

        for producto in resultados:

            print("-----------------------------")
            print("ID:", producto[0])
            print("Producto:", producto[1])
            print("Categoria:", producto[2])
            print("Stock:", producto[3])
            print("Precio:", producto[4])
            print("Proveedor:", producto[5])

        cursor.close()


def actualizar_producto():

    id_producto = int(input("Ingrese el ID del producto: "))

    nombre_producto = input("Ingrese el nuevo nombre: ")

    print("\n--- CATEGORIA ---")
    print("1. Technology")
    print("2. Food")
    print("3. Clothing")

    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        categoria = "Technology"
    elif opcion == 2:
        categoria = "Food"
    elif opcion == 3:
        categoria = "Clothing"
    else:
        print("Opcion invalida")
        return

    stock = int(input("Ingrese el nuevo stock: "))
    precio = float(input("Ingrese el nuevo precio: "))
    proveedor = input("Ingrese el nuevo proveedor: ")

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = """UPDATE productos
        SET nombre_producto=%s,
        categoria=%s,
        stock=%s,
        precio=%s,
        proveedor=%s
        WHERE idproductos=%s"""

        cursor.execute(query, (
            nombre_producto,
            categoria,
            stock,
            precio,
            proveedor,
            id_producto
        ))

        conexion.commit()

        print("El producto se actualizo correctamente")

        cursor.close()


def eliminar_producto():

    id_producto = int(input("Ingrese el ID del producto: "))

    if conexion.is_connected():

        cursor = conexion.cursor()

        query = "DELETE FROM productos WHERE idproductos=%s"

        cursor.execute(query, (id_producto,))

        conexion.commit()

        print("El producto se elimino correctamente")

        cursor.close()


def menu():

    while True:

        print("\n--- MENU PRINCIPAL ---")
        print("1. Registrar producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = int(input("Ingrese la opcion: "))

        match opcion:

            case 1:
                registrar_producto()

            case 2:
                consultar_productos()

            case 3:
                actualizar_producto()

            case 4:
                eliminar_producto()

            case 5:
                print("Saliendo del programa...")
                break

            case _:
                print("Opcion invalida")


menu()
