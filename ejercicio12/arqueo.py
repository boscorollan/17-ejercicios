class EstructuraArqueologica:
    def __init__(self, codigo, datacion, materiales):
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = materiales  # lista de strings
        self.compuesta_por = []  # lista de EstructuraArqueologica

    def agregar_subestructura(self, subestructura):
        self.compuesta_por.append(subestructura)

    def __str__(self):
        subestructuras = ', '.join([s.codigo for s in self.compuesta_por]) if self.compuesta_por else 'Ninguna'
        return (f"Estructura {self.codigo} (datación: {self.datacion})\n"
                f"Materiales: {', '.join(self.materiales)}\n"
                f"Compuesta por: {subestructuras}\n")
