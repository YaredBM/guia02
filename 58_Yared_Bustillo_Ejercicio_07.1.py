#EJERCICIO 07
#Escribir funciones que dada una cadena de caracteres:
#Devuelva solamente las letras consonantes. 
#Por ejemplo, si recibe algoritmos o logaritmos debe devolver lgrtms.

frase = input("Ingrese una palabra o frase: ")
if frase == 'x':
    exit();
else:
    nuevafrase = frase;
    vocales = ('a', 'e', 'i', 'o', 'u');
    for x in frase.lower():
        if x in vocales:
            nuevafrase = nuevafrase.replace(x,"");
    print("Nueva frase luego de retirar las vocales: ");
    print(nuevafrase);
