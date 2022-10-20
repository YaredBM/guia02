#EJERCICIO 01
print("Ejercicio 01")
palabra = str(input("Ingrese una palabra: "))

alfa = "abcdefghijklmnopqrstuvwxyz"
rdict = dict([ (x[1],x[0]) for x in enumerate(alfa) ])

letra1 = palabra[4]
if palabra[4]:
    print("El quinto caracter es: ",palabra[4])
    print("Su valor numérico es: ",rdict[palabra[4]])
elif palabra[4]:
    print("No tiene quinto caracter.")

