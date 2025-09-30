from figura import Figura
import math




class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.__radio = radio


    def get_radio(self):
        return self.__radio

    def set_radio(self, radio):
        self.__radio = radio

    def area(self):
        return math.pi * self.__radio ** 2


    def perimetro(self):
        return 2 * math.pi * self.__radio
    
    #representacion en cadena
    def __str__(self):
        return f"El área del círculo es: {self.area()} y el perímetro es: {self.perimetro()}"

