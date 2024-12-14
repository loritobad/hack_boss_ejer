class Usuario:
    """Clase que representa un usuario."""
    id_counter = 1

    def __init__(self, nombre, email, edad, altura, estudiante, cumpleaños=None, direccion=None):
        self.id = Usuario.id_counter
        Usuario.id_counter += 1
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.altura = altura
        self.estudiante = estudiante
        self.cumpleaños = cumpleaños
        self.direccion = direccion

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Email: {self.email}, Edad: {self.edad}, "
                f"Altura: {self.altura}m, Estudiante: {'Sí' if self.estudiante else 'No'}, "
                f"Cumpleaños: {self.cumpleaños}, Dirección: {self.direccion}")