#EJERCICIO 04
#Un programa que pida introducir una cadena y contar cuantas palabras hay en ella.
frase = str(input("Ingrese la frase: "))
print ("La frase original es : " + frase)
resultado = frase.count(" ")+1
print ("El numero total de palabras en la frase es: " + str(resultado))
