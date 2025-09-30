class Edificio:
    def __init__(self, nombre, tipo, ciudad, provincia, comunidad, pais, inicio_construccion,
                 material_principal, fin_construccion, consagracion_inicial, ultima_etapa_construccion,
                 consagracion_definitiva, estilos_arquitectonicos, bien_interes_cultural):
        self.nombre = nombre
        self.tipo = tipo
        self.ciudad = ciudad
        self.provincia = provincia
        self.comunidad = comunidad
        self.pais = pais
        self.inicio_construccion = inicio_construccion
        self.material_principal = material_principal
        self.fin_construccion = fin_construccion
        self.consagracion_inicial = consagracion_inicial
        self.ultima_etapa_construccion = ultima_etapa_construccion
        self.consagracion_definitiva = consagracion_definitiva
        self.estilos_arquitectonicos = estilos_arquitectonicos
        self.bien_interes_cultural = bien_interes_cultural



#representacion en cadena
    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Tipo: {self.tipo}\n"
                f"Ciudad: {self.ciudad}\n"
                f"Provincia: {self.provincia}\n"
                f"Comunidad: {self.comunidad}\n"
                f"País: {self.pais}\n"
                f"Inicio de construcción: {self.inicio_construccion}\n"
                f"Material principal: {self.material_principal}\n"
                f"Fin de construcción: {self.fin_construccion}\n"
                f"Consagración inicial: {self.consagracion_inicial}\n"
                f"Última etapa de construcción: {self.ultima_etapa_construccion}\n"
                f"Consagración definitiva: {self.consagracion_definitiva}\n"
                f"Estilos arquitectónicos: {', '.join(self.estilos_arquitectonicos)}\n"
                f"Bien de interés cultural desde: {self.bien_interes_cultural}\n")