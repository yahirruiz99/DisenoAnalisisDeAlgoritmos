def area_triangulo(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

puntos = []
with open(r"C:\Users\yairr\OneDrive\Escritorio\5Semestre\AnalisisAlgoritmos\Ejercicio4\campo.in", "r") as archivo:
    for linea in archivo:
        x, y = map(int, linea.split())
        if x == -1 and y == -1:
            break
        puntos.append((x, y))

mayor_area = 0
mejor_triangulo = ()

n = len(puntos)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a = area_triangulo(puntos[i], puntos[j], puntos[k])
            if a > mayor_area:
                mayor_area = a
                mejor_triangulo = (puntos[i], puntos[j], puntos[k])

print("Triángulo de mayor área encontrado:")
for x, y in mejor_triangulo:
    print(f"{x} {y}")
print(f"Área: {mayor_area}")

with open(r"C:\Users\yairr\OneDrive\Escritorio\5Semestre\AnalisisAlgoritmos\Ejercicio4\campo.out", "w") as salida:
    for x, y in mejor_triangulo:
        salida.write(f"{x} {y}\n")