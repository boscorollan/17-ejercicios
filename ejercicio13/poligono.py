class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.poligonos = []  # lista de Poligono

    def __str__(self):
        return f"({self.x}, {self.y})"

class Poligono:
    def __init__(self, puntos):
        if len(puntos) < 3:
            raise ValueError("Un polígono debe tener al menos 3 puntos.")
        self.puntos = puntos
        for p in puntos:
            p.poligonos.append(self)

    def __str__(self):
        return "Polígono con puntos: " + ", ".join(str(p) for p in self.puntos)

# Ejemplo: cuadrado con vértices en (0,0), (0,1), (1,1), (1,0)
p1 = Punto(0, 0)
p2 = Punto(0, 1)
p3 = Punto(1, 1)
p4 = Punto(1, 0)
cuadrado = Poligono([p1, p2, p3, p4])

print(cuadrado)
