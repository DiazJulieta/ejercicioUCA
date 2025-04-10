#crear una lista de 20 posiciones. utilizando for, agregando numeros aleatorios entre 1 y 200
import random
lista= []

for i in range(20):
    numero = random.randint(1,100)
    if numero not in lista:      #
        lista.append(numero)
longitud= len(lista) #cantidad de elemento de la lista
print(lista)


    
