import os
import platform

from gestion_de_productos import(
    gestionProductos,
    productosParaAdultos,
    productosParaInfantes)



def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("+ + + + + + + + + + +  + + + + + + + + + + ++ + + ")
    print(" + + + + + + + + + + +  + + + + + + + + + + ++ +  ")
    print("========== Menú de Gestión de Productos ==========")
    print("+ + + + + + + + + + +  + + + + + + + + + + ++ + + ")
    print(" + + + + + + + + + + +  + + + + + + + + + + ++ +  ")
    print("                                                  ")    
    print('1. Agregar Producto de  Infantes')
    print('2. Agregar Producto de Adultos')
    print('3. Buscar Producto por Codigo')
    print('4. Actualizar precio de Producto')
    print('5. Actualizar stock de Producto')
    print('6. Eliminarar Producto por codigo')
    print('7. Mostrar Todos los Productos')
    print('8. Salir')
    print("                                                  ")
    print('==================================================')


def agregar_producto(gestion, tipo_producto):
    try:
        nombre = input('Ingrese nombre del producto: ')
        precio = input('Ingrese precio del producto: ')
        cantidad_en_stock = input('Ingrese cantidad del producto en stock: ')
        codigo_de_productos =input('Ingrese codigo del producto: ')#no gusrda el numero '0'
        

        if tipo_producto == '1':
            rango_etario = input(' 0: bebes \n 1: Kits \n 2: Juniors \n Ingrese la opcion correspondiente al rango etario del producto: ')
            producto = productosParaInfantes( nombre, precio, cantidad_en_stock, codigo_de_productos, rango_etario)
        elif tipo_producto == '2':
            genero = input(' 1: Masculino \n 2: Femenino \n 3: Unisex \n Ingrese la opcion correspondiente al genero del producto: ')
            producto = productosParaAdultos(nombre, precio, cantidad_en_stock, codigo_de_productos , genero)
        else:
            print('Opción inválida')
            return

        gestion.crear_producto(producto)
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')

    except Exception as e:
        print(f'Error inesperado: {e}')


def buscar_producto_por_codigo(gestion):
    codigo= input('Ingrese el codigo del producto a buscar: ')
    producto = gestion.leer_producto(codigo)
    if producto:
        print(producto)
    input('Presione enter para continuar...')



def actualizar_precio_producto(gestion):
    codigo= input('Ingrese el codigo del producto para actualizar precio: ')
    precio_nuevo = input('Ingrese el precio nuevo: ')
    gestion.actualizar_precio(codigo, precio_nuevo)
    gestion.mostrar_producto(codigo)
    input('Presione enter para continuar...')

def actualizar_stock_producto(gestion):
    codigo= input('Ingrese el codigo del producto para actualizar Stock: ')
    nuevo_stock = input('Ingrese el stock nuevo: ')
    gestion.actualizar_stock(codigo, nuevo_stock)
    gestion.mostrar_producto(codigo)
    input('Presione enter para continuar...')

def eliminar_producto_por_codigo(gestion):
    codigo = input('Ingrese el codigo del colaborador a eliminar: ')
    gestion.eliminar_producto(codigo)
    input('Presione enter para continuar...')

def mostrar_todos_los_productos(gestion):
    print('=============== Listado completo de los Productos ==============')
    for producto in gestion.leer_datos().values():
        if 'rango_etario' in producto:
            print(f"Producto: {producto['nombre']} \nRango_etario {producto['rango_etario']}")
        else:
            print(f"Producto: {producto['nombre']} \nGenero: {producto['genero']}")
    print('=====================================================================')
    input('Presione enter para continuar...')


if __name__ == "__main__":
    archivo_productos = 'productos_db.json'
    gestion = gestionProductos(archivo_productos)

    while True:
        #limpiar_pantalla() #limpia antes de mostrar el mensaje de error
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_producto(gestion, opcion) 
        
        elif opcion == '3' :
            buscar_producto_por_codigo(gestion)

        elif opcion == '4' :
            actualizar_precio_producto(gestion)

        elif opcion == '5' :
            actualizar_stock_producto(gestion)

        elif opcion == '6' :
            eliminar_producto_por_codigo(gestion)

        elif opcion == '7' :
            mostrar_todos_los_productos(gestion)

        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')
        
        
       