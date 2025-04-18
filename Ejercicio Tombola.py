import random

bolillero = list(range(0,46))

def sacar_numeros(bolillero):
    numeros_sorteados=[]
    for i in range(6):
        numero=random.choice(bolillero)
        numeros_sorteados.append(numero)
        bolillero.remove(numero)
    return numeros_sorteados
        
jugador1=[3,15,22,30,35,42]
jugador2=[1,12,18,25,33,40]
jugador3=[5,10,20,28,36,44]

numeros_sorteados=sacar_numeros(bolillero)

aciertos_jugador1=set(jugador1) & set(numeros_sorteados)
aciertos_jugador2=set(jugador2) & set(numeros_sorteados)
aciertos_jugador3=set(jugador3) & set(numeros_sorteados)

print("numeros sorteados:",numeros_sorteados)
print("jugador 1:",jugador1,"aciertos:",aciertos_jugador1)
print("jugador 2:",jugador2, "aciertos:",aciertos_jugador2)
print("jugador 3:",jugador3, "aciertos:",aciertos_jugador3)
