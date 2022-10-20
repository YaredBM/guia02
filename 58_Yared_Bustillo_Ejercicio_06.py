#EJERCICIO 06
frase = str(input("Ingresa una frase: "))
palabras = frase.split()
contar_letra_palabra = {p:len(p) for p in palabras}
print(contar_letra_palabra)
