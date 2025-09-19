def contarDigitos(numeroEntero):
    if numeroEntero < 10:
        return 1
    else:
        return 1 + contarDigitos(numeroEntero // 10)

numeroEntero = 123456789
resultado = contarDigitos(numeroEntero)
print("Cantidad de dígitos: ", resultado)
