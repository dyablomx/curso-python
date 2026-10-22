palabra = input("Escribe una palabra: ")
contador = 0

for letra in palabra:
    #.lower convierte cada letra a minúscula para reconocer también las vocales mayúsculas.
    if letra.lower() in "aeiou":
        contador = contador + 1

print(f"La palabra {palabra} contiene {contador} vocales.")