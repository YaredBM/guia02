#EJERCICIO 06
#Escriba un programa que lea una frase y a continuación visualice cada palabra 
#de la frase en columnas, seguida del número de letras que tiene cada palabra.
frase = str(input("Ingresa una frase: "))
palabras = frase.split()
contar_letra_palabra = {p:len(p) for p in palabras}
print(contar_letra_palabra)
