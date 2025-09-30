class Persona:
    def __init__(self, nombre, apellido1, apellido2=None, fecha_nacimiento=None, sexo=None, num_id=None):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.num_id = num_id
        self.padres = []   # 0..2, rol: progenitor
        self.hijos = []    # 0..N, rol: descendiente
        self.conyuge = None  # 0..1, rol: pareja

    def agregar_padre(self, padre):
        if len(self.padres) < 2:
            self.padres.append(padre)
            padre.hijos.append(self)

    def casar_con(self, persona):
        self.conyuge = persona
        persona.conyuge = self

class Padre(Persona):
    pass

class Madre(Persona):
    pass

class Hijo(Persona):
    pass

class Conyuge(Persona):
    pass

# Ejemplo de uso con herencia y relaciones familiares
if __name__ == "__main__":
    carlos = Padre("Carlos", "Windsor")
    diana = Madre("Diana", "de Gales", apellido2="Spencer")
    guillermo = Hijo("Guillermo", "Windsor")
    kate = Conyuge("Kate", "Windsor", apellido2="Middleton")

    guillermo.agregar_padre(carlos)
    guillermo.agregar_padre(diana)
    guillermo.casar_con(kate)

    print(f"Padres de Guillermo: {[p.nombre for p in guillermo.padres]}")
    print(f"Hijos de Carlos: {[h.nombre for h in carlos.hijos]}")
    print(f"Cónyuge de Guillermo: {guillermo.conyuge.nombre}")
    print(f"Cónyuge de Kate: {kate.conyuge.nombre}")
