def add_prod(inventario):
    name = input("Ingrese el nombre del producto: ").lower()
    cant = int(input("Ingrese la cantidad: "))
    if name in inventario:
        inventario[name] += cant
    else:
        inventario[name] = cant
    
    return inventario

def del_prod(inventario):
    name = input("Ingrese el nombre del producto que desea eliminar: ").lower()
    if name in inventario: 
        del inventario[name]
        print("Producto eliminado!")
    else:
        print("No se encontró el producto ingresado.")

    return inventario

def show_inv(inventario):
    for clave, valor in inventario.items():
        print(f"Producto: {clave}, Stock: {valor}")
    print()

