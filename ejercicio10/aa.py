# Definición de clases (resumido)
class Persona:
    def __init__(self, nombre, rol, email):
        self.nombre = nombre
        self.rol = rol
        self.email = email

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []
    def agregar_miembro(self, persona):
        self.miembros.append(persona)

class Tarea:
    def __init__(self, titulo, responsable, estado):
        self.titulo = titulo
        self.responsable = responsable
        self.estado = estado

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = None
        self.tareas = []
    def asignar_equipo(self, equipo):
        self.equipo = equipo
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear personas
    ana = Persona("Ana López", "Desarrolladora", "ana@empresa.com")
    juan = Persona("Juan Pérez", "Analista", "juan@empresa.com")

    # Crear equipo y añadir miembros
    equipo = Equipo("Equipo Backend")
    equipo.agregar_miembro(ana)
    equipo.agregar_miembro(juan)

    # Crear tareas
    tarea1 = Tarea("Diseño de base de datos", juan, "En progreso")
    tarea2 = Tarea("Implementación API", ana, "Pendiente")

    # Crear proyecto y asociar tareas y equipo
    proyecto = Proyecto("Sistema de Gestión")
    proyecto.asignar_equipo(equipo)
    proyecto.agregar_tarea(tarea1)
    proyecto.agregar_tarea(tarea2)

    # Mostrar información
    print(f"Proyecto: {proyecto.nombre}")
    print(f"Equipo: {proyecto.equipo.nombre}")
    print("Miembros:")
    for miembro in proyecto.equipo.miembros:
        print(f"  - {miembro.nombre} ({miembro.rol})")
    print("Tareas:")
    for tarea in proyecto.tareas:
        print(f"  - {tarea.titulo}: {tarea.estado} (Responsable: {tarea.responsable.nombre})")
