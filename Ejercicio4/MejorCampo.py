from itertools import combinations
import os

ruta = os.path.dirname(os.path.abspath(__file__))

def area_triangulo(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

def cruz(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

puntos = []
with open(os.path.join(ruta, "campo.in"), "r") as archivo:
    for linea in archivo:
        x, y = map(int, linea.split())
        if x == -1 and y == -1:
            break
        puntos.append((x, y))

puntos.sort()

parte1 = []
for p in puntos:
    while len(parte1) >= 2 and cruz(parte1[-2], parte1[-1], p) <= 0:
        parte1.pop()
    parte1.append(p)

parte2 = []
for p in reversed(puntos):
    while len(parte2) >= 2 and cruz(parte2[-2], parte2[-1], p) <= 0:
        parte2.pop()
    parte2.append(p)

hull = parte1[:-1] + parte2[:-1]

mayor = 0
mejor = None

for a, b, c in combinations(hull, 3):
    area = area_triangulo(a, b, c)
    if area > mayor:
        mayor = area
        mejor = (a, b, c)

print("Triángulo de mayor área encontrado:")
for x, y in mejor:
    print(f"{x} {y}")

with open(os.path.join(ruta, "campo.out"), "w") as salida:
    for x, y in mejor:
        salida.write(f"{x} {y}\n")