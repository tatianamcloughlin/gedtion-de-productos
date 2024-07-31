
# Desafío 1: Sistema de Gestión de Productos
# Objetivo: Desarrollar un sistema para manejar productos en un inventario.

# Requisitos:

# Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
# Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
# Implementar operaciones CRUD para gestionar productos del inventario.
# Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
# Persistir los datos en archivo JSON.


import json

class Producto :
    def __init__(self, nombre, precio, cantidad_en_stock, codigo_de_productos):
        self.__nombre = nombre
        self.__precio = self.validar_precio(precio)
        self.__cantidad_en_stock = self.validar_cantidad_en_stock(cantidad_en_stock)
        self.__codigo_de_productos = self.validar_codigo_de_productos(codigo_de_productos)

    @property
    def nombre(self):
         return self.__nombre.capitalize()

    @property
    def precio(self):
         return self.__precio

    @property
    def cantidad_en_stock(self):
         return self.__cantidad_en_stock

    @property
    def codigo_de_productos(self):
         return self.__codigo_de_productos

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)

    @cantidad_en_stock.setter
    def cantidad_en_stock(self,nuevo_stock):
        self.__cantidad_en_stock= self.validar_cantidad_en_stock(nuevo_stock)


    def validar_precio(self,precio):
        try:
            precio_num = float(precio)
            if precio_num <= 0 :
                raise ValueError("El precio o debe ser numéro positivo.")#no anda, no se muestra(salta el exept)
            return precio_num
        except ValueError: 
            raise ValueError("el precio debe ser un numero.")
        
 
    def validar_codigo_de_productos(self,codigo_de_productos):
        try:
            codigo_de_productos_num = int(codigo_de_productos)
            if len(str(codigo_de_productos)) != 8 :
                raise ValueError(f"el codigo ingresado debe tener 8 numeros")
            if codigo_de_productos_num <= 0:
                raise ValueError("El codigo del producto debe ser un numéro positivo.") #no anda, no se muestra(salta el exept)
                
            return codigo_de_productos_num
        except ValueError:
            raise ValueError ("El codigo del producto debe ser un numero.")


    def validar_cantidad_en_stock(self,cantidad_en_stock):
        try:
            cantidad = int(cantidad_en_stock)
            if cantidad <=0:
               raise ValueError ("cantidad en stock ingresada no valida ") #no anda, no se muestra(salta el exept)
            return cantidad 
        except ValueError: 
            raise ValueError ("la cantidad en stock debe ser un numero .") 
 
    
    def to_dict(self):
        return { 
            "nombre": self.nombre,
            "cantidad_en_stock": self.cantidad_en_stock,
            "precio": self.precio,
            "codigo_de_productos": self.codigo_de_productos
        }

    def __str__(self):
        return f"Producto:{self.nombre} \nPrecio: ${self.precio} \nStock disponible:{self.cantidad_en_stock} "

class productosParaInfantes(Producto):
    def __init__(self, nombre, precio, cantidad_en_stock, codigo_de_productos, rango_etario):
        super().__init__(nombre, precio, cantidad_en_stock, codigo_de_productos)
        self.__rango_etario = self.validar_rango_etario(rango_etario)
   

    @property
    def rango_etario(self):
        #return self.__rango_etario
        if self.__rango_etario == "0":
            return "Bebes"
        elif self.__rango_etario == "1":
            return "Kids"
        elif self.__rango_etario == "2":
            return "Juniors"
        
    def validar_rango_etario(self, rango_etario):
        try:
            #rango = int(rango_etario)
            if rango_etario not in ["0", "1", "2", "Bebes", "Kids", "Juniors"]:
                raise ValueError("La opción ingresada no corresponde a ningún rango etario existente")
            return rango_etario
        except ValueError:
            raise ValueError("El valor ingresado es incorrecto o no corresponde a ningún rango etario existente")
        except TypeError:
            raise TypeError("El argumento ingresado es del tipo incorrecto")

    def to_dict(self):
        data = super().to_dict()
        data["rango_etario"] = self.rango_etario
        return data

    def __str__(self):
        return f"{super().__str__()} \nRango_etario: {self.rango_etario}"  


class productosParaAdultos(Producto):
    def __init__(self, nombre, precio, cantidad_en_stock, codigo_de_productos , genero):
        super().__init__(nombre, precio, cantidad_en_stock, codigo_de_productos)
        self.__genero = self.validar_genero(genero)


    @property
    def genero(self):
        if self.__genero == "1":
            return "Masculino"
        elif self.__genero == "2":
            return "Femenino"
        elif self.__genero == "3":
            return "Unisex"

    
    def validar_genero(self, genero):
        try:
            if genero not in ["1", "2", "3","Masculino","Femenino","Unisex" ]:
                raise ValueError("La opción ingresada no corresponde a ningún género existente")
            return genero
        except ValueError:
            raise ValueError("La opción ingresada no corresponde a ningún género existente")
        except TypeError:
            raise TypeError("El argumento ingresado es del tipo incorrecto")

        
    def to_dict(self):
        data = super().to_dict()
        data["genero"] = self.genero
        return data

    def __str__(self):
        return f"{super().__str__()} \nGenero: {self.genero}" 
    
class gestionProductos:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')



    def crear_producto(self, producto):
        try:
            datos = self.leer_datos()
            codigo = producto.codigo_de_productos
            if not str(codigo) in datos.keys():
                datos[codigo] = producto.to_dict()
                self.guardar_datos(datos)
                print(f"producto {producto.nombre} fue creado correctamente.")
            else:                    print(f"Ya existe producto con codigo de producto '{codigo}'.")
        except Exception as error:
            print(f'Error inesperado al crear producto: {error}')

    def leer_producto(self, codigo_de_producto):
        try:
            datos = self.leer_datos()
            if codigo_de_producto in datos.keys():
                producto_data = datos[codigo_de_producto]
                if 'genero' in producto_data:
                    producto = productosParaAdultos(**producto_data)
                else:
                    producto = productosParaInfantes(**producto_data)
                print(f'Producto encontrado con codigo {codigo_de_producto}')
            
            else:
                print(f'No se encontró producto con codigo {codigo_de_producto}')
                return None
            return producto
        except TypeError:
            raise ("El argumento ingresado es del tipo incorrecto")
        except Exception as e:
            print(f'Error al leer producto: {e}')
            return None
        
    def actualizar_precio(self, codigo_de_producto, nuevo_precio):
        try:
            datos = self.leer_datos() 
            n_precio = float(nuevo_precio)
            if codigo_de_producto in datos.keys():
                datos[codigo_de_producto]['precio'] = n_precio #como valido, si ingreso una letra se rompe el codigo xq no puede convertirlo en float, no llega a la validacion_codigo_de_producto?
                self.guardar_datos(datos)
                print(f'Precio actualizado para el producto de codigo:{codigo_de_producto}')
            else:
                 print(f'No se encontró producto de codigo:{codigo_de_producto}')
        except Exception as e:
            print(f'Error al actualizar el producto: {e}')

    def mostrar_producto(self,codigo_de_producto):
        try:
            datos = self.leer_datos()
            producto_data = datos[codigo_de_producto]
            if 'genero' in producto_data:
                producto = productosParaAdultos(**producto_data)
            else:
                producto = productosParaInfantes(**producto_data)
            print (producto)
            return producto
        except Exception as e:
            print(f'Error al mostrar el producto: {e}')



    def actualizar_stock(self, codigo_de_producto, nuevo_stock):
        try:
            datos = self.leer_datos()
            n_stock = int(nuevo_stock)
            if codigo_de_producto in datos.keys():
                datos[codigo_de_producto]['cantidad_en_stock'] = n_stock #como valido, si ingreso una letra se rompe el codigo xq no puede convertirlo en int, no llega a la validacion_precio?
                self.guardar_datos(datos)
                print(f'Stock actualizado para el producto de codigo:{codigo_de_producto}')
            else:
                 print(f'No se encontró producto de codigo:{codigo_de_producto}')
        except Exception as e:
            print(f'Error al actualizar el producto: {e}')




    def eliminar_producto(self, codigo_de_producto):
        try:
            datos = self.leer_datos()
            if codigo_de_producto in datos.keys():
                del datos[codigo_de_producto]
                self.guardar_datos(datos)
                print(f'producto con codigo:{codigo_de_producto} eliminado correctamente')
            else:
                print(f'No se encontró producto con codigo:{codigo_de_producto}')
        except Exception as e:
            print(f'Error al eliminar el producto: {e}')
