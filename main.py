#aqui vamos a correr todos los ejercicios

#ejercicio 1
from ejercicio1.circulo import Circulo
from ejercicio1.rectangulo import Rectangulo
from ejercicio1.figura import Figura
from ejercicio1.cuadrado import Cuadrado
from ejercicio1.elipse import Elipse


circuloBosco = Circulo(5)
print(circuloBosco)
Rectangulo=Rectangulo(4,6)
print(Rectangulo)
cuadrado=Cuadrado(4)
print(cuadrado)
eli=Elipse(6,4)
print(eli)   













#ejercicio 6
from ejercicio6.personaje import Persona  

if __name__ == "__main__":
    persona1 = Persona("Juan", "Gonzalez", "Heredia", "01/01/1990", "M", "12345678A")
    yo = Persona("Bosco", "Rollán", "Agudo", "20/07/2006", "M", "87654321B")
    print(yo)
    print(persona1)
    print(yo.saludar())
    print(yo.despedirse("Ana"))

