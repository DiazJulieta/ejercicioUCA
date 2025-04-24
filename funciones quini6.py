#funciones:
   # generar la grilla
import random
def generar_grilla():
    grilla=[]
    for i in range(46):
         grilla.append(i)
    return grilla
   # generar la grilla del jugador
def generar_player():
    return random.sample(range(46), 6)

player1=generar_player
player2=generar_player
   # sorteo
def sorteo_quini6(grilla, player1 , player2):
    sorteo=[]
    while grilla and player1 and player2:
        numero_sorteo = random.choice(grilla) #pedir que guarde un numero aleatorio
        sorteo.append(numero_sorteo)
        print(f"Numero sorteado: {numero_sorteo}") #guardar en grilla
        
        if numero_sorteo in player1:
            player1.remove(numero_sorteo)
            print("player1 tenia el numero")#si sale el numero eliminarlo de la grilla
            
        if numero_sorteo in player2:
            player2.remove(numero_sorteo)
            print("player2 tenia el numero")
            
        grilla.remove(numero_sorteo) #para asegurarme que el numero no salga hay que eliminarlo de la grilla
    return sorteo, player1 , player2
    
   # mostar resultados
def mostrar_resultados(sorteo, player1, player2):
      print("\n Números sorteados:", sorteo)
      print("Player1 restantes:", player1)
      print("Player2 restantes:", player2)
      
      if not player1 and not player2:
          print("¡Empate! Ambos jugadores completaron sus números al mismo tiempo.")
      elif not player1:
          print("¡Player 1 ganó!")
      elif not player2:
          print("¡Player 2 ganó!")
def main(): #desde donde debe arrancar el programa
    grilla=generar_grilla()
    player1=generar_player()
    player2=generar_player()
    
    print("player1: ",player1)
    print("player2: ", player2)
    
    sorteo,restante1,restante2=sorteo_quini6(grilla,player1, player2)
    mostrar_resultados(sorteo,restante1,restante2)
    
if __name__=="__main__":
    main()

