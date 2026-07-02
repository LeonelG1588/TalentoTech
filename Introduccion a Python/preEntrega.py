from rich import print

carrito = []
opcion = 0


while opcion != 5:

    print("")
    print("== MENU [bold reverse green]'tienda generica'[/bold reverse green] ==")
    print("1.Agregar producto/s al carrito.")
    print("2.Mostrar producto/s.")
    print("3.Buscar un producto/s.")
    print("4.Eliminar un producto/s.")
    print("5.Salir del programa.")
    print("")


    opcion = input("Ingrese una opcion: ")
    while not opcion.isdecimal() or int(opcion) <= 0 or int(opcion) > 5:
        print("Opcion invalida. Ingrese un numero (1-5).")
        opcion = input("Ingrese una opcion: ")

    opcion = int(opcion)

    match opcion:

        #CARGA DE DATOS.
        case 1:
            print("")
            fin = ""
            while fin.lower() != "fin":

                nombre = input("Ingrese el nombre del producto: ")
                while nombre == "":
                    print("El campo no puede estar vacio.")
                    nombre = input("Ingrese el nombre del producto: ") 

                nombre = nombre.title()   

                categoria = input("Ingrese la categoria del producto: ")
                while categoria == "":
                    print("El campo no puede estar vacio.")
                    categoria = input("Ingrese la categoria del producto: ")

                categoria = categoria.title()

                precio = input("Ingrese el precio del producto: ")
                while not precio.isdecimal() or int(precio) <= 0 or precio == "":
                    print("Ingrese un valor decimal que sea mayor a 0")
                    precio = input("Ingrese el precio del producto: ")

                producto = {"nombre" : nombre,"categoria" : categoria, "precio" : int(precio)}
                carrito.append(producto)
                print("\nProducto/s cargado/s correctamente.\n")
            
                fin = input("Ingrese 'fin' para la dejar de cargar productos: \n") 

            print("Volviendo al menu...")
            enter = input()

        #MUESTREO DE DATOS.                
        case 2:
            print("")
            if len(carrito) == 0:
                print("No hay productos cargados.")
                print("Volviendo al menu...")
                enter = input()

            else:
            
                for i,items in enumerate(carrito):
                    print(f"#{i+1}\n Nombre = {items.get('nombre')}\n Categoria = {items.get('categoria')}\n Precio = ${items.get('precio')}")

                print("Volviendo al menu...")
                enter = input()
            

        #BUSQUEDA Y MUESTRO DE DATOS.
        case 3:
            print("")
            if len(carrito) == 0:
                print("No hay productos cargados.")
                print("Volviendo al menu...")
                enter = input()

            else:

                fin = ""
                while fin.lower() != "fin":

                    productoBuscado = input("Ingrese el nombre del producto que desea buscar: ")
                    while productoBuscado == "":
                        print("El campo no puede estar vacio.")
                        productoBuscado = input("Ingrese el nombre del producto que desea buscar: ")

                    productoBuscado = productoBuscado.title()

                    encontrado = False

                    for i,items in enumerate(carrito):
                        if(productoBuscado == items.get('nombre')):
                            print(f"\nProducto encontrado en posicion #{i+1}:")
                            print(f" Nombre = {items.get('nombre')}\n Categoria = {items.get('categoria')}\n Precio = ${items.get('precio')}\n")
                            encontrado = True
                            break

                    if not encontrado:
                        print("No se ha encontrado ese producto.\n")

                    fin = input("Ingrese 'fin' para la dejar de buscar productos: \n") 

                print("Volviendo al menu...")
                enter = input()

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
            print("Muchas gracias por comprar en 'tienda generica'.")
            
            


