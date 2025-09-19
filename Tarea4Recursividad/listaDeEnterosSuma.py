def suma(lista):
    if lista == []:   
        print("La lista esta vacía")
        return 0
    else:
        print("Sumando", lista[0], "con el resto de números:", lista[1:])
        resultado_parcial = lista[0] + suma(lista[1:])
        return resultado_parcial

# Creamos una lista de números
numeros = [10, 20, 30, 40, 50, 1]

# Calculamos la suma
print("Iniciando la suma recursiva:)")
resultado = suma(numeros)
print("Resultado final de la suma:", resultado)
