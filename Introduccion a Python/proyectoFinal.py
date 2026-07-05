from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from rich.align import Align
from rich.text import Text
import time


console = Console()
console.clear()

opcion = 0
lstProductos = [{
        "id": 1, 
        "nombre": "Teclado Mecánico", 
        "descripcion": "Teclado RGB con switches red", 
        "cantidad": 15, 
        "precio": 45.50, 
        "categoria": "Periféricos"
    },
    {
        "id": 2, 
        "nombre": "Mouse Óptico", 
        "descripcion": "Mouse inalámbrico ergonómico", 
        "cantidad": 3, 
        "precio": 20.00, 
        "categoria": "Periféricos"
    },
    {
        "id": 3, 
        "nombre": "Monitor Gamer", 
        "descripcion": "Monitor 24 pulgadas 144Hz", 
        "cantidad": 2, 
        "precio": 180.00, 
        "categoria": "Monitores"
    }]


def volverMenu():
    console.print("[dim #ff8800]Presione [bold white]'enter'[/] para volver al menu...[/]")
    input()

def preguntarContinuar(mensaje):
    
    while True:
        resp = input(mensaje).strip().upper()
        if resp in ["S", "N"]:
            return resp
        console.print("❌[red]Opción invalida. Ingrese 'S' o 'N'.[/]\n")

def mostrarMenu():
    console.print(
        Panel.fit(
            "[bold white]SISTEMA DE GESTION DE PRODUCTOS[/bold white]",
            border_style="green"
        )
    )

    console.print(
        Panel.fit(
            "[bold cyan]1.[/][white]Agregar producto/s.\n"
            "[bold cyan]2.[/][white]Mostrar producto/s.[/]\n"
            "[bold cyan]3.[/][white]Actualizar producto/s.[/]\n"
            "[bold cyan]4.[/][white]Eliminar producto/s.[/]\n"
            "[bold cyan]5.[/][white]Buscar producto/s.[/]\n"
            "[bold cyan]6.[/][white]Generar reporte.[/]\n"
            "[bold cyan]7.[/][white]Salir del programa.[/]",
            title="[bold white]Menu Principal[/]",
            border_style="blue"
        )
    )

def elegirOpcion(minimo,maximo):

    while True:
        try:
            opcion = int(input("Ingrese una de las opciones: ").strip())

            if opcion < minimo or opcion > maximo:
                console.print(f"❌[red] Opción invalida. Ingrese un número entre: {minimo} y {maximo}.[/]\n")
            else:
                return opcion
        except ValueError:
            console.print("❌[red] Debe ingresar un numero valido.[/]\n")

    

def hayProductos():
    hayProductos = True
    if not lstProductos:
        hayProductos = False
    return hayProductos

def generarId():
    if not lstProductos:
        idI = 1
    else:
        idI = lstProductos[-1]["id"] + 1
    return int(idI)

def pedirId():
    if not hayProductos():
        console.print(
            "[bold red]No hay productos cargados.[/]"
        )
        return None
    
    while True:
        try:
            idBuscado = int(input("Ingrese el 'id' del producto: ").strip())

            if idBuscado < 1:
                console.print("❌[red]Opción invalida. Debe ingresar un numero mayor a 0.[/]\n")
                continue
        
            idsExistentes = [p["id"] for p in lstProductos]
            if idBuscado not in idsExistentes:
                console.print(f"❌[red]El producto con id=[{idBuscado}] no existe.[/]\n")
                console.print(f"[blue]IDs de productos disponibles: {idsExistentes}[/]\n")
                continue

            console.print("[blue]Encontrado.[/]👍\n")
            return idBuscado
        
        except ValueError:
            console.print("❌[red]Opción invalida. Ingrese un numero entero valido[/]\n")

def pedirNombre():

    while True:
        nombre = input("Ingrese el nombre del producto: ").strip().title()

        if nombre == "":
            console.print("❌[red] El campo no puede estar vacio.[/]\n")
        elif not nombre.replace(" ","").isalpha():
            console.print("❌[red] El campo solo puede contener letras.[/]\n")
        else:
            return nombre
    
def pedirDescripcion():
    descripcion = input("Ingrese una descripcion del producto: ").strip().lower()
    return descripcion

def pedirCantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: ").strip())

            if cantidad <= 0:
                console.print("❌[red] La cantidad debe ser mayor a 0.[/]\n")
            else:
                return cantidad
        except ValueError:
            console.print("❌[red] Debe ingresar un numero valido.[/]\n")
    
def pedirPrecio():
    while True:
        try:
            precio = float(input("Ingrese el precio: ").strip())

            if precio <= 0:
                console.print("❌[red] El precio debe ser mayor a 0.[/]\n")
            else:
                return precio
        except ValueError:
            console.print("❌[red] Debe ingresar un numero valido.[/]\n")

    
def pedirCategoria():

    while True:
        categoria = input("Ingrese la categoria del producto: ").strip().title()

        if categoria == "":
            console.print("❌[red] El campo no puede estar vacio.[/]\n")
        elif not categoria.replace(" ","").isalpha():
            console.print("❌[red] El campo solo puede contener letras.[/]\n")
        else:
            return categoria


def agregarProducto():

    idI = generarId()
    nombre = pedirNombre() 
    categoria = pedirCategoria()
    cantidad = pedirCantidad()
    precio = pedirPrecio()
    descripcion = pedirDescripcion()

    producto = {"id" : idI,
                "nombre" : nombre,
                "categoria" : categoria,
                "cantidad" : cantidad, 
                "precio" : precio,
                "descripcion" : descripcion,}
        
    lstProductos.append(producto)
    console.print("[bold green]\nProducto/s cargado/s correctamente ✅\n[/]")
            
    respuesta = preguntarContinuar("¿Desea agregar otro producto? (S/N): ")

    if respuesta == "S":
        agregarProducto()
    else:
        volverMenu()    
    
def mostrarProductos():
    if not hayProductos():
        console.print(
            "[bold red]No hay productos cargados.[/]"
        )
    else:
        tabla = Table(
            show_lines=True,
            header_style="bold white",
            border_style="bright_yellow"
            )
        tabla.add_column("ID", style="bold white", justify="center")
        tabla.add_column("Nombre", style="bold white", justify="center")
        tabla.add_column("Categoria", style="bold white", justify="center")
        tabla.add_column("Precio", style="bold white", justify="center")
        tabla.add_column("Cantidad", style= "bold white", justify="right")
        tabla.add_column("Descripcion", style="bold white")

        for producto in lstProductos:
            tabla.add_row(
                str(f"[white]{producto['id']}[/]"),
                producto["nombre"],
                producto["categoria"],
                f"${producto['precio']:.2f}",
                str(producto['cantidad']),
                producto["descripcion"]
            )
        console.print(tabla)
    volverMenu()


def buscarProducto(idBuscado):
    tabla = Table(
        header_style="bold white",
        border_style="bright_yellow"
    )
    tabla.add_column("ID", style="bold white", justify="center")
    tabla.add_column("Nombre", style="bold white", justify="center")
    tabla.add_column("Categoria", style="bold white", justify="center")
    tabla.add_column("Precio", style="bold white", justify="center")
    tabla.add_column("Cantidad", justify="right")
    tabla.add_column("Descripcion", style="bold white")
    
    for i,producto in enumerate(lstProductos):
        if producto["id"] == idBuscado:  
            console.print(f"[blue]Producto encontrado en la posicion:[/] [cyan]{i+1}[/]\n")
            if producto["cantidad"] <= 10:
                cantidad = f"[blink red]{producto['cantidad']}[/]"
            else:
                cantidad = f"[bold green]{producto['cantidad']}[/]"
            tabla.add_row(
                str(f"[white]{producto['id']}[/]"),
                producto["nombre"],
                producto["categoria"],
                f"${producto['precio']:.2f}",
                cantidad,
                producto["descripcion"]
            )
            console.print(tabla)
            break
    
    volverMenu()

def actualizarProducto(idBuscado):
    
    tabla = Table(
        header_style="bold white",
        border_style="bright_yellow"
    )
    tabla.add_column("ID", style="bold white", justify="center")
    tabla.add_column("Nombre", style="bold white", justify="center")
    tabla.add_column("Categoria", style="bold white", justify="center")
    tabla.add_column("Precio", style="bold white", justify="center")
    tabla.add_column("Cantidad", justify="right")
    tabla.add_column("Descripcion", style="bold white")
    
    for i,producto in enumerate(lstProductos):
        if producto["id"] == idBuscado:  
            console.print(f"[blue]Producto encontrado en la posicion:[/] [cyan]{i+1}[/]\n")
            if producto["cantidad"] <= 10:
                cantidad = f"[blink red]{producto['cantidad']}[/]"
            else:
                cantidad = f"[bold green]{producto['cantidad']}[/]"
            tabla.add_row(
                str(f"[white]{producto['id']}[/]"),
                producto["nombre"],
                producto["categoria"],
                f"${producto['precio']:.2f}",
                cantidad,
                producto["descripcion"]
            )
            console.print(tabla)
            break

    console.print(
        Panel.fit(
            "[bold #d260ff]1.[/][white]Modificar nombre.[/]\n"
            "[bold #d260ff]2.[/][white]Modificar categoria.[/]\n"
            "[bold #d260ff]3.[/][white]Modificar cantidad.[/]\n"
            "[bold #d260ff]4.[/][white]Modificar precio.[/]\n"
            "[bold #d260ff]5.[/][white]Modificar descripcion.[/]\n"
            "[bold #d260ff]6.[/][white]Volver al menu.[/]",
            title="[bold white]Menu[/]",
            border_style="#b700ff"
        )
    )
    
    
    opcion = elegirOpcion(1,6)
    
    match opcion:

        case 1:
            print("")
            for producto in lstProductos:
                    if producto["id"] == idBuscado:
                        producto["nombre"] = pedirNombre()
                        break
            console.print("[bold green]Nombre actualizado correctamente.[/]✅\n")

        case 2:
            print("")
            for producto in lstProductos:
                if producto["id"] == idBuscado:
                    producto["descripcion"] = pedirDescripcion()
                    break
            console.print("[bold green]Descripcion actualizada correctamente.[/]✅\n")

        case 3:
            print("")
            for producto in lstProductos:
                if producto["id"] == idBuscado:
                    producto["cantidad"] = pedirCantidad()
                    break
            console.print("[bold green]Cantidad actualizada correctamente.[/]✅\n")

        case 4:
            print("")
            for producto in lstProductos:
                if producto["id"] == idBuscado:
                    producto["precio"] = pedirPrecio()
                    break
            console.print("[bold green]Precio actualizado correctamente.[/]✅\n")

        case 5:
            print("")
            for producto in lstProductos:
                if producto["id"] == idBuscado:
                    producto["categoria"] = pedirCategoria()
                    break
            console.print("[bold green]Categoria actualizada correctamente.[/]✅\n")

        case 6:
            print("")
        
    respuesta = preguntarContinuar(f"¿Desea actualizar otro campo del producto con id {idBuscado}? (S/N): ")

    if respuesta == "S":
        console.clear()
        actualizarProducto(idBuscado)
    else:
        volverMenu()


def eliminarProducto(idBuscado):
    global lstProductos
    
    cantProductos = len(lstProductos)
    lstProductos = [p for p in lstProductos if p["id"] != idBuscado]
    

    if len(lstProductos) < cantProductos:
        console.print(f"[green]Producto con id=[{idBuscado}] eliminado correctamente.[/]✅\n")

    
    if not hayProductos():
        console.print("[blue]No quedan productos por eliminar.[/]")
    else:
        print(f"[blue]Cantidad de productos actuales:[/] [cyan]{len(lstProductos)}[/]\n")

    volverMenu() 


def establecerMinimo():
    cantidadMin = pedirCantidad()
    return cantidadMin



def generarReporteStock(min):
    if not hayProductos():
        console.print(
            "[bold red]No hay productos cargados.[/]]"
        )
    else:
        tabla = Table(
        show_lines=True,
        header_style="bold white",
        border_style="bright_yellow"
        )
        tabla.add_column("ID", style="bold white", justify="center")
        tabla.add_column("Nombre", style="bold white", justify="center")
        tabla.add_column("Categoria", style="bold white", justify="center")
        tabla.add_column("Precio", style="bold white", justify="center")
        tabla.add_column("Cantidad", justify="right")
        tabla.add_column("Descripcion", style="bold white")
        
        cantBajoStock = 0
        lstProductosBajoStock = []
        
        for i,producto in enumerate(lstProductos):
            if producto["cantidad"] <= min:
                cantBajoStock+=1
                lstProductosBajoStock.append(producto["id"])
                console.print(f"⚠️[blink yellow] Producto con bajo stock en la posicion:{i+1}![/]")
                cantidad = f"[blink red]{producto['cantidad']}[/]"
                
                tabla.add_row(
                    str(f"[white]{producto['id']}[/]"),
                    producto["nombre"],
                    producto["categoria"],
                    f"${producto['precio']:.2f}",
                    cantidad,
                    producto["descripcion"]
                )
                
        if cantBajoStock == 0:
            console.print(f"[blue]No se encontraron productos con stock menor o igual a[/] [cyan]{min}[/]")
            volverMenu()
        else:
            console.print(tabla)
            console.print(f"[blue]Hay[/] [cyan]{cantBajoStock}[/] [blue]producto/s con bajo stock.[/]")
            
            respuesta = preguntarContinuar("¿Desea reabastecer algun producto? (S/N): ")

            if respuesta == "S":
                reabastecerStock(lstProductosBajoStock)
            else:
                volverMenu()  
                

def reabastecerStock(lstProdBajoStock):
    console.rule("[bold cyan]REABASTECER STOCK[/]")

    while True:
        try:
            idBuscado = int(input("Ingrese el 'id' del producto con bajo stock: ").strip())

            if idBuscado not in lstProdBajoStock:
                console.print(f"❌[red] Opción invalida. El id={idBuscado} no tiene bajo stock o no existe.[/]\n")
                console.print(f"[blue]IDs de productos que puedes reabastecer:[/] [cyan]{lstProdBajoStock}[/]")
                continue
            break
        except ValueError:
            console.print("❌[red]Ingrese un numero entero valido.[/]\n")

    for producto in lstProductos:
        if producto["id"] == idBuscado:
            cantidadAReabastecer = pedirCantidad()

            producto["cantidad"] += cantidadAReabastecer

            console.print(f"[green]Stock actualizado correctamente.✅[/] [white]|[/] [blue]Nuevo stock:[/] [cyan]{producto['cantidad']}[/].")
            break
    
    volverMenu()
    
def animacion():
    texto = "TALENTO TECH"

    colores = [
    "red",
    "yellow",
    "green",
    "cyan",
    "blue",
    "magenta",
    ]

    with Live(refresh_per_second=15, console=console) as live:

        for desplazamiento in range(60):

            titulo = Text(style="bold")

            for i, letra in enumerate(texto):
                color = colores[(i + desplazamiento) % len(colores)]
                titulo.append(letra, style=f"bold {color}")

            live.update(Align.center(titulo))
            time.sleep(0.10)

animacion()

while opcion != 7:

    
    mostrarMenu()

    opcion = elegirOpcion(1,7)

    match opcion:

        case 1:
            console.rule("[bold cyan]AGREGAR PRODUCTO[/]")
            agregarProducto()
            console.clear()
        case 2:
            console.rule("[bold cyan]MOSTRAR PRODUCTOS[/]")
            mostrarProductos()
            console.clear()
        case 3:
            console.rule("[bold cyan]ACTUALIZAR PRODUCTO[/]")
            idBuscado = pedirId()
            if idBuscado == None:
                volverMenu()
                continue
            actualizarProducto(idBuscado)
            console.clear()
        case 4:
            console.rule("[bold cyan]ELIMINAR PRODUCTO[/]")
            idBuscado = pedirId()
            if idBuscado == None:
                volverMenu()
                continue
            eliminarProducto(idBuscado)
            console.clear()

        case 5:
            console.rule("[bold cyan]BUSCAR PRODUCTO[/]")
            idBuscado = pedirId()
            if idBuscado == None:
                volverMenu()
                continue
            buscarProducto(idBuscado)
            console.clear()
        case 6:
            console.rule("[bold cyan]GENERAR REPORTE DE STOCK[/]")
            generarReporteStock(establecerMinimo())
            console.clear()
        case 7:
            console.print("[bold red]Saliendo del sistema...[/]")
            
            


