class Persona:
    def __init__(self, nombre, apellido, apellido_soltera=None, titulo=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_soltera = apellido_soltera
        self.titulo = titulo
        self.padres = []
        self.cónyuge = None

    def set_padres(self, padre1, padre2):
        self.padres = [padre1, padre2]

    def casar_con(self, persona):
        self.cónyuge = persona
        persona.cónyuge = self

    def __str__(self):
        padres_str = ', '.join([p.nombre for p in self.padres]) if self.padres else 'Desconocidos'
        conyuge_str = self.cónyuge.nombre if self.cónyuge else 'Ninguno'
        return f"{self.nombre} {self.apellido} (Título: {self.titulo if self.titulo else '-'}, Apellido soltera: {self.apellido_soltera if self.apellido_soltera else '-'}, Padres: {padres_str}, Cónyuge: {conyuge_str})"

# Crear objetos
carlos = Persona("Carlos", "Windsor", titulo="de Gales")
diana = Persona("Diana", "de Gales", apellido_soltera="Spencer")
guillermo = Persona("Guillermo", "Windsor", titulo="de Gales")
kate = Persona("Kate", "Windsor", apellido_soltera="Middleton")

guillermo.set_padres(carlos, diana)
guillermo.casar_con(kate)

# Mostrar diagrama de objetos
print(guillermo)
print(kate)
print(carlos)
print(diana)
