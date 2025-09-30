class Cuadro:
    def __init__(self, titulo, adscripcion_cronologica, tecnica, subtecnica, soporte, autor, estado_conservacion, institucion, ciudad, pais, replica_de=None):
        self.titulo = titulo
        self.adscripcion_cronologica = adscripcion_cronologica
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.autor = autor
        self.estado_conservacion = estado_conservacion
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais
        self.replica_de = replica_de

    def __str__(self):
        return (f"Título: {self.titulo}\n"
                f"AC: {self.adscripcion_cronologica}\n"
                f"Técnica: {self.tecnica}\n"
                f"Sub-técnica: {self.subtecnica}\n"
                f"Soporte: {self.soporte}\n"
                f"Autor: {self.autor}\n"
                f"Estado de conservación: {self.estado_conservacion}\n"
                f"Institución: {self.institucion}\n"
                f"Ciudad: {self.ciudad}\n"
                f"País: {self.pais}\n"
                f"Réplica de: {self.replica_de.titulo if self.replica_de else 'Ninguna'}\n")

# Crear objetos
la_gioconda = Cuadro(
    titulo="La Gioconda",
    adscripcion_cronologica="1503 - 1516",
    tecnica="Óleo",
    subtecnica="Sfumato",
    soporte="Madera de álamo",
    autor="Leonardo da Vinci",
    estado_conservacion="Regular",
    institucion="Museo del Louvre",
    ciudad="París",
    pais="Francia"
)

gioconda_prado = Cuadro(
    titulo="Gioconda de El Prado",
    adscripcion_cronologica="1503 - 1516",
    tecnica="Óleo",
    subtecnica="Pincelada simple",
    soporte="Madera de nogal",
    autor="Desconocido",
    estado_conservacion="Bueno",
    institucion="Museo de El Prado",
    ciudad="Madrid",
    pais="España",
    replica_de=la_gioconda
)

print(la_gioconda)
print(gioconda_prado)
