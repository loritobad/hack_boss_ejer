from controlador.users import imprimir_usuario_por_email, imprimir_usuarios, imprimir_usuarios_ordenados, crear_usuario, actualizar_usuario, borrar_usuario_por_email, borrar_todos_usuarios, guardar_usuarios_csv

def menu():
    usuarios = []
    while True:
        print("\nMenú de opciones:")
        print("1. Imprimir todos los usuarios")
        print("2. Imprimir usuarios ordenados por edad")
        print("3. Imprimir un usuario por email")
        print("4. Crear un nuevo usuario")
        print("5. Actualizar un usuario existente")
        print("6. Borrar un usuario por email")
        print("7. Borrar todos los usuarios")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                imprimir_usuarios(usuarios)
            elif opcion == "2":
                imprimir_usuarios_ordenados(usuarios)
            elif opcion == "3":
                imprimir_usuario_por_email(usuarios)
            elif opcion == "4":
                usuarios.append(crear_usuario())
                guardar_usuarios_csv(usuarios)
            elif opcion == "5":
                actualizar_usuario(usuarios)
                guardar_usuarios_csv(usuarios)
            elif opcion == "6":
                borrar_usuario_por_email(usuarios)
                guardar_usuarios_csv(usuarios)
            elif opcion == "7":
                borrar_todos_usuarios(usuarios)
                guardar_usuarios_csv(usuarios)
            elif opcion == "8":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")