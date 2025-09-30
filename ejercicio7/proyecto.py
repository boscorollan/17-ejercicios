# Definición de clases (ver respuesta anterior)
class Persona:
    """Representa a un miembro del equipo de proyecto."""
    def __init__(self, nombre, rol, email):
        self.nombre = nombre
        self.rol = rol
        self.email = email

class Tarea:
    """Representa una tarea dentro de un proyecto."""
    def __init__(self, titulo, descripcion, responsable, fecha_inicio, fecha_fin, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.responsable = responsable  # objeto Persona
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

class Equipo:
    """Grupo de personas que trabajan en el proyecto."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_miembro(self, persona):
        self.miembros.append(persona)

class Proyecto:
    """Representa un proyecto profesional."""
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, estado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.tareas = []
        self.equipo = None

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def asignar_equipo(self, equipo):
        self.equipo = equipo

