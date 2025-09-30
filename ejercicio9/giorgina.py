class Cuadro:
    def __init__(self, titulo, representado, autor, lugar_pintado, existen_copias, tecnica, soporte, ubicacion_actual, estado_conservacion):
        self.titulo = titulo
        self.representado = representado
        self.autor = autor
        self.lugar_pintado = lugar_pintado
        self.existen_copias = existen_copias
        self.tecnica = tecnica
        self.soporte = soporte
        self.ubicacion_actual = ubicacion_actual
        self.estado_conservacion = estado_conservacion

    def __str__(self):
        return (f"Cuadro: {self.titulo}\n"
                f"Representa a: {self.representado}\n"
                f"Autor: {self.autor}\n"
                f"Lugar pintado: {self.lugar_pintado}\n"
                f"¿Existen copias?: {'Sí' if self.existen_copias else 'No'}\n"
                f"Técnica: {self.tecnica}\n"
                f"Soporte: {self.soporte}\n"
                f"Ubicación actual: {self.ubicacion_actual}\n"
                f"Estado de conservación: {self.estado_conservacion}")


