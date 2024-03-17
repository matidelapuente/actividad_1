print("Elija la opción deseada:")
print("1 - Agregar nuevo producto.")
print("2 - Eliminar producto existente.")
print("3 - Mostrar inventario actual.")

selection = input()

dict = {}

while selection != "x":

    if selection == "1":
        name = input("Ingrese el nombre del producto o # para volver al menu principal: ").lower()
        while name != "#":
            cant = int(input("Ingrese la cantidad: "))
            if name in dict:
                dict[name] += cant
            else:
                dict[name] = cant
            name = input("Ingrese el nombre del producto o # para volver al menu principal: ").lower()

    elif selection == "2":
        name = input("Ingrese el nombre del producto que desea eliminar: ").lower()
        if name in dict: 
            del dict[name]
            print("Producto eliminado!")
        else:
            print("No se encontró el producto ingresado.")

    elif selection == "3":
        print(dict)

    elif selection.lower() == "x":
        break

    else: 
        print("La opcion ingresada no es valida.")
    
    print("Elija la opción deseada:")
    print("1 - Agregar nuevo producto.")
    print("2 - Eliminar producto existente.")
    print("3 - Mostrar inventario actual.")
    print("X - Salir.")
    selection = input()