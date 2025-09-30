from alpha import Cuadro

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
#representacion en cadena
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
