class ActuacionArqueologica:
    """
    Representa una actuación arqueológica.
    Atributos:
        fecha_inicio: Fecha de inicio de la actuación.
        fecha_fin: Fecha de fin de la actuación.
        tipo: Tipo de actuación (sondeo, excavación o seguimiento).
    """
    def __init__(self, fecha_inicio, fecha_fin, tipo):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo

    def __str__(self):
        return (f"Actuación arqueológica ({self.tipo}): "
                f"del {self.fecha_inicio} al {self.fecha_fin}")
    
#crea un ejemplo de uso
