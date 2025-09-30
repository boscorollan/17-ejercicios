from figura import Figura
import math

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.__lado = lado

    def get_lado(self):
        return self.__lado

    def set_lado(self, lado):
        self.__lado = lado

    def area(self):
        return self.__lado ** 2

    def perimetro(self):
        return 4 * self.__lado
