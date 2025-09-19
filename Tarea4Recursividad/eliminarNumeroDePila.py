def eliminarNumeroDeEnmedio(pila, medio, actual=0):
    if actual == medio:
        pila.pop()
        return

    tope = pila.pop()
    eliminarNumeroDeEnmedio(pila, medio, actual + 1)
    pila.append(tope)

pila = [8, 2, 3, 4, 20, 100, 7, 5, 121]   
n = len(pila)
if n > 0:
    k = (n-1) // 2
    medio = n-1 - k
    print("Pila original:", pila)
    eliminarNumeroDeEnmedio(pila, medio)
    print("Pila sin el número de en medio:", pila)
else:
    print("Pila vacía")
