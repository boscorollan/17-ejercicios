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



#EJERCICIO 2
from ejercicio2.al import Persona
carlos = Persona("Carlos", "Windsor", titulo="de Gales")
diana = Persona("Diana", "de Gales", apellido_soltera="Spencer")
guillermo = Persona("Guillermo", "Windsor", titulo="de Gales")
kate = Persona("Kate", "Windsor", apellido_soltera="Middleton")

guillermo.set_padres(carlos, diana)
guillermo.casar_con(kate)

print(guillermo)
print(kate)
print(carlos)
print(diana)


#EJERCICIO 3
from ejercicio3.alpha import Cuadro
from ejercicio3.gioconda import la_gioconda
from ejercicio3.gioconda_prado import gioconda_prado

print(la_gioconda)
print(gioconda_prado)


#EJERCICIO 4
from catedral import Edificio

if __name__ == "__main__":


    catedral_santiago = Edificio("Catedral de Santiago de Compostela", "Templo de culto católico", "Santiago de Compostela"
    , "La Coruña", "Galicia", "España", 1075, "granito", 1122, 1128, 1168, "3 de abril de 1211",
      ["Románico", "Gótico", "Barroco", "Plateresco", "Neoclásico"], 1896)
    print(catedral_santiago)


#EJERCICIO 5
# --- Instanciación de objetos de las clases de figuras ---
from ejercicio1.circulo import Circulo
from ejercicio1.rectangulo import Rectangulo
from ejercicio1.cuadrado import Cuadrado
from ejercicio1.elipse import Elipse

# Círculo negro de radio 1
circulo = Circulo(1)
print('Objeto círculo:', circulo)

# Rectángulo naranja de longitud 3 y anchura 1
rectangulo = Rectangulo(3, 1)
print('Objeto rectángulo:', rectangulo)

# Cuadrado azul de lado 1.5
cuadrado = Cuadrado(1.5)
print('Objeto cuadrado:', cuadrado)

# Elipse amarilla de eje mayor 3 y eje menor 1
elipse = Elipse(3, 1)
print('Objeto elipse:', elipse)

#EJERCICIO 6
from ejercicio6.personaje import Persona

Bosco = Persona("Bosco", "Rollán", "Agudo","27 de julio de 2006", "AAAAAAb1")
print(bosco.despedirse("Ana"))





























#ejercicio 6
from ejercicio6.personaje import Persona  

if __name__ == "__main__":
    persona1 = Persona("Juan", "Gonzalez", "Heredia", "01/01/1990", "M", "12345678A")
    yo = Persona("Bosco", "Rollán", "Agudo", "20/07/2006", "M", "87654321B")
    print(yo)
    print(persona1)
    print(yo.saludar())
    print(yo.despedirse("Ana"))

