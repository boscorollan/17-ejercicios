class Cuadro:
    def __init__(self, titulo, adscripcion_cronologica, tecnica, subtecnica, soporte, autor, estado_conservacion, institucion, ciudad, pais, es_replicade=None):
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
        self.es_replicade = es_replicade  # 0..1 referencia a otro Cuadro
        self.replicas = []  # 0..N lista de Cuadro
        if es_replicade:
            es_replicade.replicas.append(self)

    def __str__(self):
        return (f"Cuadro: {self.titulo}\n"
                f"Técnica: {self.tecnica}, Sub-técnica: {self.subtecnica}\n"
                f"Soporte: {self.soporte}\n"
                f"Autor: {self.autor}\n"
                f"Institución: {self.institucion}, Ciudad: {self.ciudad}, País: {self.pais}\n"
                f"Estado de conservación: {self.estado_conservacion}\n"
                f"Réplica de: {self.es_replicade.titulo if self.es_replicade else 'Ninguna'}\n"
                f"Réplicas: {[r.titulo for r in self.replicas] if self.replicas else 'Ninguna'}\n")

# Ejemplo de uso:
if __name__ == "__main__":
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
        es_replicade=la_gioconda
    )
    print(la_gioconda)
    print(gioconda_prado)
