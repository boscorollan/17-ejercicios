from figura import Figura
import math

class Elipse(Figura):
    def __init__(self, eje_mayor, eje_menor):
        super().__init__("Elipse")
        self.__eje_mayor = eje_mayor
        self.__eje_menor = eje_menor

    def get_eje_mayor(self):
        return self.__eje_mayor

    def set_eje_mayor(self, eje_mayor):
        self.__eje_mayor = eje_mayor

    def get_eje_menor(self):
        return self.__eje_menor

    def set_eje_menor(self, eje_menor):
        self.__eje_menor = eje_menor

    def area(self):
        return math.pi * (self.__eje_mayor / 2) * (self.__eje_menor / 2)

    def perimetro(self):
        # Aproximación de Ramanujan
        a = self.__eje_mayor / 2
        b = self.__eje_menor / 2
        return math.pi * (3*(a+b) - math.sqrt((3*a+b)*(a+3*b)))

