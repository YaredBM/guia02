#EJERCICIO 03
#Un programa que pida una cadena y la imprima al revés
def reverso(x):
  return x[::-1]

frase = reverso(str(input("Ingrese una frase: ")))
print(frase)
