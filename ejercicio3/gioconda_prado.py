from alpha import Cuadro
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

print(la_gioconda)
print(gioconda_prado)
