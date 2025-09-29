#aqui vamos a correr todos los ejercicios

#ejercicio 6
from ejercicio6.personaje import Persona  

if __name__ == "__main__":
    persona1 = Persona("Juan", "Gonzalez", "Heredia", "01/01/1990", "M", "12345678A")
    yo = Persona("Bosco", "Rollán", "Agudo", "20/07/2006", "M", "87654321B")
    print(yo)
    print(persona1)
    print(yo.saludar())
    print(yo.despedirse("Ana"))

