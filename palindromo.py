palindromo = False
while not palindromo:
    Palabra = input("Ingrese una palabra para saber si es palindromo: ")
    Palabra = Palabra.lower()
    for i in range(len(Palabra) // 2):
        if Palabra[i] != (Palabra[-( i + 1 )]):
            es_palindromo = False
            break
        else:
            es_palindromo = True

    if es_palindromo:
        print(f"{Palabra} es palíndromo")
        palindromo = True

    else:
        print(f"{Palabra} no es palíndromo")