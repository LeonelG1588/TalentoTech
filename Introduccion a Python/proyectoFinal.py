import os

carrito = []
opcion = 0

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def generarId():
    if not carrito:
        return 1

    return carrito[-1]["id"] + 1

def volverMenu():
    enter = input("Presione 'enter' para volver al menu.")

def agregarProducto():
    fin = ""
    while fin.lower() != "fin":

        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            print("El campo no puede estar vacio.")
            nombre = input("Ingrese el nombre del producto: ").strip()
        nombre = nombre.title()   

        categoria = input("Ingrese la categoria del producto: ").strip()
        while categoria == "":
            print("El campo no puede estar vacio.")
            categoria = input("Ingrese la categoria del producto: ").strip()
        categoria = categoria.title()

        precio = input("Ingrese el precio del producto: ").strip()
        while not precio.isdecimal() or int(precio) <= 0:
            print("Ingrese un numero entero que sea mayor a 0")
            precio = input("Ingrese el precio del producto: ").strip()

        iD = generarId()
        
        producto = {"id" : iD,"nombre" : nombre,"categoria" : categoria, "precio" : int(precio)}
        carrito.append(producto)
        print("\nProducto/s cargado/s correctamente.\n")
            
        fin = input("Escriba 'fin' para la dejar de cargar productos, o presione 'enter' para continuar: \n").strip().lower()
    volverMenu()
    
def mostrarProducto():
    if not carrito:
        print("No hay productos cargados.")
    else:
            
        for i,producto in enumerate(carrito):
            print(f"""
        Id : {producto["id"]}
        Nombre : {producto["nombre"]}
        Categoria : {producto["categoria"]}
        Precio : {producto["precio"]}
        """)
            
    volverMenu()


def buscarProducto(iD):
    encontrado = False
    for i, producto in enumerate(carrito):
        if producto["id"] == iD:
            encontrado = True
            return i, producto

    return encontrado




while opcion != 7:

    print("")
    print("== MENU 'tienda generica' ==")
    print("1.Agregar producto/s al carrito.")
    print("2.Mostrar producto/s.")
    print("3.Actualizar producto/s.")
    print("4.Eliminar producto/s.")
    print("5.Buscar producto/s.")
    print("6.Generar reporte.")
    print("7.Salir del programa.")
    print("")


    opcion = input("Ingrese una opcion: ")
    while not opcion.isdecimal() or int(opcion) <= 0 or int(opcion) > 7:
        print("Opción invalida. Ingrese un número (1-7).")
        opcion = input("Ingrese una opción: ")

    opcion = int(opcion)

    match opcion:

        #CARGA DE DATOS.
        case 1:
            print("")
            agregarProducto()
            cls()

        #MUESTREO DE DATOS.                
        case 2:
            print("")
            mostrarProducto()
            cls()
            

        #ACTUALIZACION DE DATOS
        case 3:
            print("")


        #BUSQUEDA Y ELIMINACION DE DATOS.
        case 4:
            print("")
            if len(carrito) == 0:
                print("No hay productos cargados.")
                print("Volviendo al menu...")
                enter = input()

            else:

                fin = ""
                while fin.lower() != "fin":

                    indice = input("Ingrese el numero del producto que desea eliminar: ")
                    while not indice.isdecimal() or int(indice) < 1 or int(indice) > len(carrito):
                        print(f"El numero ingresado no es valido. Tiene que ser un valor entre 1 y {len(carrito)}\n")
                        indice = input("Ingrese el numero del producto que desea eliminar: ") 
                    
                    indice = int(indice) - 1
                    productoEliminado = carrito.pop(indice)
                    print(f"\n{productoEliminado.get('nombre')} en la posicion #{indice+1} eliminado correctamente.\n")

                    if len(carrito) == 0:
                        print("Ya no quedan productos en el carrito.")
                        break

                    fin = input("Ingrese 'fin' para la dejar de eliminar productos: \n")

                
                print("Volviendo al menu...")
                enter = input()

        case 5:
            print("")
            iD = input("Ingrese el id del producto: ").strip()
            while iD == "":
                print("El campo no puede estar vacio.")
                iD = input("Ingrese el id del producto: ").strip()

            iD = int(iD)

            resultado = buscarProducto(iD)

            if resultado:
                posicion, producto = resultado
                print(f"""
            Producto encontrado en posicion: #{posicion+1}
            Id : {producto["id"]}
            Nombre : {producto["nombre"]}
            Categoria : {producto["categoria"]}
            Precio : {producto["precio"]}
            """)
            else: 
                print("No se encontró el producto.")
            volverMenu()
        case 6:
            print("Muchas gracias por comprar en 'tienda generica'.")
        case 7:
            print("Muchas gracias por comprar en 'tienda generica'.")
            
            


