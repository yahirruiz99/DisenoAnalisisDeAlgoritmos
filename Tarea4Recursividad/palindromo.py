def esPalindromo(cadena):
    if len(cadena) <= 1:
        return "es palindromo"
    
    primera_letra = cadena[0]
    ultima_letra = cadena[-1]
    
    if primera_letra != ultima_letra:
        return "no es palindromo"
    
    cadena_reducida = cadena[1:-1]
    
    return esPalindromo(cadena_reducida)

palabra1 = "seres"
palabra2 = "pancha"

print(palabra1, "->", esPalindromo(palabra1))
print(palabra2, "->", esPalindromo(palabra2))