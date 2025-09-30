from ejercicio13.poligono import Punto, Poligono

# Definición de puntos
pA = Punto(0, 0)
pB = Punto(1, 0)
pC = Punto(0, 1)
pD = Punto(1, 1)

# Triángulo 1: ABC
triangulo1 = Poligono([pA, pB, pC])
# Triángulo 2: ABD
triangulo2 = Poligono([pA, pB, pD])

print("Triángulo 1:", triangulo1)
print("Triángulo 2:", triangulo2)

# Mostrar a cuántos polígonos pertenece cada punto
print(f"Punto A pertenece a {len(pA.poligonos)} polígonos")
print(f"Punto B pertenece a {len(pB.poligonos)} polígonos")
print(f"Punto C pertenece a {len(pC.poligonos)} polígonos")
print(f"Punto D pertenece a {len(pD.poligonos)} polígonos")
