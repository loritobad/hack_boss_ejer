import csv
from datetime import date
from entidades.user import Usuario
from entidades.addres import Address


def guardar_usuarios_csv(usuarios, archivo="usuarios.csv"):
    """Guarda los usuarios en un archivo CSV."""
    
    with open(archivo, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nombre", "Email", "Edad", "Altura", "Estudiante", "Cumpleaños", "Dirección"])
        for usuario in usuarios:
            writer.writerow([
                usuario.id, usuario.nombre, usuario.email, usuario.edad,
                usuario.altura, usuario.estudiante, usuario.cumpleaños, usuario.direccion
            ])

def imprimir_usuarios(usuarios):
    """Imprime los usuarios en consola."""
    if not usuarios:
        print("No hay usuarios registrados.")
    for usuario in usuarios:
        print(usuario)

def imprimir_usuarios_ordenados(usuarios):
    """Imprime los usuarios ordenados por edad."""
    
    orden = input("Ordenar por edad: ascendente (a) o descendente (d): ").lower()
    usuarios_ordenados = sorted(usuarios, key=lambda x: x.edad, reverse=(orden == 'd'))
    imprimir_usuarios(usuarios_ordenados)

def imprimir_usuario_por_email(usuarios):
    """Imprime un usuario por email."""
    email = input("Ingrese el email del usuario: ")
    usuario = next((u for u in usuarios if u.email == email), None)
    if usuario:
        print(usuario)
    else:
        print("Usuario no encontrado.")
        
def crear_usuario():
    """crea un usuario a partir de la entrada del usuario."""
    nombre = input("Nombre: ")
    email = input("Email: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura (en metros): "))
    estudiante = input("Es estudiante (sí/no): ").strip().lower() == "sí"

    cumpleaños = None
    if input("¿Desea ingresar la fecha de cumpleaños? (sí/no): ").strip().lower() == "sí":
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        año = int(input("Año: "))
        cumpleaños = date(año, mes, dia)

    direccion = None
    if input("¿Desea ingresar una dirección? (sí/no): ").strip().lower() == "sí":
        street = input("Calle: ")
        city = input("Ciudad: ")
        country = input("País: ")
        direccion = Address(street, city, country)

    return Usuario(nombre, email, edad, altura, estudiante, cumpleaños, direccion)

def actualizar_usuario(usuarios):
    email = input("Ingrese el email del usuario a actualizar: ")
    usuario = next((u for u in usuarios if u.email == email), None)
    if not usuario:
        print("Usuario no encontrado.")
        return

    print("Deje el campo vacío para no cambiar el valor actual.")
    usuario.nombre = input(f"Nombre [{usuario.nombre}]: ") or usuario.nombre
    usuario.edad = int(input(f"Edad [{usuario.edad}]: ") or usuario.edad)
    usuario.altura = float(input(f"Altura [{usuario.altura}]: ") or usuario.altura)
    usuario.estudiante = input(f"Es estudiante (sí/no) [{usuario.estudiante}]: ").strip().lower() == "sí"
    print("Usuario actualizado correctamente.")

def borrar_usuario_por_email(usuarios):
    email = input("Ingrese el email del usuario a borrar: ")
    usuario = next((u for u in usuarios if u.email == email), None)
    if usuario:
        usuarios.remove(usuario)
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")

def borrar_todos_usuarios(usuarios):
    usuarios.clear()
    print("Todos los usuarios han sido eliminados.")