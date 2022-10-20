#EJERCICIO 07.2
frase_n = str(input("Ingrese una palabra o frase: "))
print("La frase original es : " + str(frase_n))
vocal = 'a e i o u'.split()
tem = dict(zip(vocal, vocal[1:] + [vocal[0]]))
resultado = "".join([tem.get(ele, ele) for ele in frase_n])
print("The replaced string : " + str(resultado))
