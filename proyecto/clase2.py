# lista = [numero **2 for numero in range (0,11)]
#
# print (lista)
#
# lista2 = [numero **2 for numero in range (0,11) if numero %2 == 0]
# print (lista2)

# doblar = lambda num: num*2
#
# print (doblar(2))

#recursividad

def factorial(numero):
    if numero == 0:
        return 1
    else:
#        print(f"soy el numero {numero}")
        # recur = factorial (numero -1)
        # resultado = recur * numero
        # return resultado
        return factorial (numero -1) * numero
print(factorial(5))
