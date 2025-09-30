#aqui vamos a correr todos los ejercicios

#ejercicio 1
from ejercicio1.circulo import Circulo
from ejercicio1.rectangulo import Rectangulo
from ejercicio1.figura import Figura
from ejercicio1.cuadrado import Cuadrado
from ejercicio1.elipse import Elipse

mi_circulo = Circulo(5)
print(f"El área del círculo es: {mi_circulo.area():.2f}")
print(f"El perímetro del círculo es: {mi_circulo.perimetro():.2f}")

#ejercicio 6
from ejercicio6.personaje import Persona  

if __name__ == "__main__":
    persona1 = Persona("Juan", "Gonzalez", "Heredia", "01/01/1990", "M", "12345678A")
    yo = Persona("Bosco", "Rollán", "Agudo", "20/07/2006", "M", "87654321B")
    print(yo)
    print(persona1)
    print(yo.saludar())
    print(yo.despedirse("Ana"))

