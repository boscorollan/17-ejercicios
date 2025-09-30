class Planta:
    def __init__(self, numero, capacidad_estanterias):
        self.numero = numero
        self.capacidad_estanterias = capacidad_estanterias  # número máximo de libros
        self.libros = []  # lista de Libros

class Libro:
    def __init__(self, identificador, tematica):
        self.identificador = identificador  # único
        self.tematica = tematica
        self.ejemplares = []  # lista de Ejemplar

class Ejemplar:
    def __init__(self, id_ejemplar):
        self.id_ejemplar = id_ejemplar
        self.prestamo = None  # objeto Prestamo si está prestado

class Prestamo:
    def __init__(self, ejemplar, lector, fecha_prestamo, fecha_entrega, max_dias):
        self.ejemplar = ejemplar
        self.lector = lector
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega
        self.max_dias = max_dias

class Lector:
    def __init__(self, id_lector, nombre, direccion):
        self.id_lector = id_lector  # identificación o pasaporte
        self.nombre = nombre
        self.direccion = direccion
        self.fichas = []  # historial de préstamos

class Empleado(Lector):
    def __init__(self, id_lector, nombre, direccion, id_empleado):
        super().__init__(id_lector, nombre, direccion)
        self.id_empleado = id_empleado  # identificación de empleado

# Ejemplo de instanciación
if __name__ == "__main__":
    # Crear plantas
    planta1 = Planta(1, 1000)
    planta2 = Planta(2, 1200)
    planta3 = Planta(3, 800)

    # Crear libros y ejemplares
    libro1 = Libro("ISBN123", "Narrativa")
    ejemplar1 = Ejemplar("EJ1")
    ejemplar2 = Ejemplar("EJ2")
    libro1.ejemplares.extend([ejemplar1, ejemplar2])
    planta1.libros.append(libro1)

    # Crear lectores
    lector1 = Lector("12345678A", "Juan Pérez", "Calle Mayor 1")
    empleado1 = Empleado("87654321B", "Ana López", "Calle Menor 2", "EMP001")

    # Crear préstamo
    from datetime import date, timedelta
    prestamo1 = Prestamo(ejemplar1, lector1, date.today(), date.today() + timedelta(days=30), 30)
    ejemplar1.prestamo = prestamo1
    lector1.fichas.append(prestamo1)

    # Mostrar información
    print(f"Planta 1 capacidad: {planta1.capacidad_estanterias} libros")
    print(f"Libro en planta 1: {libro1.identificador}, temática: {libro1.tematica}")
    print(f"Ejemplar prestado: {ejemplar1.id_ejemplar} a {prestamo1.lector.nombre}")
    print(f"Empleado: {empleado1.nombre}, ID empleado: {empleado1.id_empleado}")
