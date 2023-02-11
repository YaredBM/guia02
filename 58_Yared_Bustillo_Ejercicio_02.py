#EJERCICIO 02
#Leer una frase y contar el número de vocales (de cada una) que aparecen.
while(True):
    frase = input('Ingresa la frase: ')
    if frase == 'fin': 
        quit()
    lower = str.lower(frase)
    convert = list(lower)
    a = convert.count('a')
    e = convert.count('e')
    i = convert.count('i')
    o = convert.count('o')
    u = convert.count('u')

    vowel = a + e + i + o + u

    print ('Total de vocales = ', vowel)
    print ('a = ', a)
    print ('e = ', e)
    print ('i = ', i)
    print ('o = ', o)
    print ('u = ', u)
    print(" ")
