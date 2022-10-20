#EJERCICIO 07
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
