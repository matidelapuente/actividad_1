import f_inv

def menu():
    print("---Menú de opciones---")
    print()
    print("1 - Agregar nuevo producto.")
    print("2 - Eliminar producto existente.")
    print("3 - Mostrar inventario actual.")
    print("4 - Salir.")
    print()


def main ():
    inventario = {}
    while True:
        menu()
        option = input("Seleccione una opción: ")
        print()

        match option:
            case "1":
                inventario = f_inv.add_prod(inventario)
            case "2":
                inventario = f_inv.del_prod(inventario)
            case "3":
                f_inv.show_inv(inventario)
            case "4":
                print("Hasta luego!")
                break
            case _: 
                print("Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()