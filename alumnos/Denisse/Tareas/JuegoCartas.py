jugador1=[1,10,7,5,1] #jugador 1 con posicion 0
jugador2=[9,5,8,6,5] #jugador 2 con posicion 1
jugador3=[9,9,7,8,4] #jugadpr 3 con posicion 2
jugador4=[5,2,2,9,3] #jugador 4 con posicion 3
jugada=[] #Lista de jugada vacia
puntos_finales=[] #Lista de puntos finales vacio
num_juego=1 #Numero de Jugadas
ronda=4 #Numero de rondas y posicion en las listas
#Puntos de jugadores
ptsjug1=0
ptsjug2=0
ptsjug3=0
ptsjug4=0
max_carta=0 #carta mas alta
carta_rep=0 #numero de veces carta mas alta repetida
num_jugador=0 #posicion de la carta (numero de jugador)
carta=0 #carta repetida
max_pts=0 #ganador del juego(puntos acumulados)
rep_pts=0 #ganadores empatados
pts=0 #punto por ronda
pos=0 #posicion tabla final puntos
put=0 #puntos tabla final

while ronda>=0 and ronda<=4:
  jugada.append(jugador1[ronda]) 
  jugada.append(jugador2[ronda])
  jugada.append(jugador3[ronda])
  jugada.append(jugador4[ronda])
  max_carta=max(jugada)
  carta_rep=jugada.count(max_carta)
  if carta_rep==1:
        num_jugador=jugada.index(max_carta) # posicion de la carta(numero del jugador)
        num_jugador=num_jugador+1 # numero de jugador real
        print("Ronda # "+ str(num_juego) + " : "+ str(jugada))
        if num_jugador==1:
          pts=1
          ptsjug1=ptsjug1+pts #suma de puntos
          print("El Jugador No."+ str(num_jugador)+ " Gano con la carta: "+ str(max_carta)+ " Puntos: "+ str(pts)+ " Acumulados: " + str(ptsjug1)+"\n")
        elif num_jugador==2:
          pts=1
          ptsjug2=ptsjug2+pts #suma de puntos
          print("El Jugador No."+ str(num_jugador)+ " Gano con la carta: "+ str(max_carta)+ " Puntos: "+ str(pts)+ " Acumulados: "+ str(ptsjug2)+ "\n")
        elif num_jugador==3:
          pts=1
          ptsjug3=ptsjug3+pts #suma de puntos
          print("El Jugador No."+ str(num_jugador)+ " Gano con la carta: "+ str(max_carta)+ " Puntos: "+ str(pts)+ " Acumulados: "+ str(ptsjug3)+ "\n")  
        elif num_jugador==4:
          pts=1
          ptsjug4=ptsjug4+pts #suma de puntos
          print("El Jugador No."+ str(num_jugador)+ " Gano con la carta: "+ str(max_carta)+ " Puntos: "+ str(pts)+ " Acumulados: "+ str(ptsjug4)+ "\n")
  if carta_rep!=1:
          print("Ronda # "+ str(num_juego) + " : "+ str(jugada))
          for num_jugador, carta in enumerate(jugada) : #la posicion(numero de jugador) y carta repetida
            if max_carta==carta:
              num_jugador=num_jugador+1
              if num_jugador==1:
                pts=1
                ptsjug1=ptsjug1+pts
                print("El jugador No."+ str(num_jugador)+" con la carta: "+ str(carta)+ " Puntos: "+ str(pts)+ " Acumulados: "+ str(ptsjug1))
              elif num_jugador==2:
                pts=1
                ptsjug2=ptsjug2+pts
                print("El jugador No."+ str(num_jugador)+" con la carta: "+ str(carta)+ " Puntos: "+ str(pts)+ " Acumulados: "+ str(ptsjug2))
              elif num_jugador==3:
                pts=1
                ptsjug3=ptsjug3+pts
                print("El jugador No."+ str(num_jugador)+" con la carta: "+ str(carta)+ " Puntos: "+ str(pts)+ " Acumulados: "+ str(ptsjug3))
              elif num_jugador==4:
                pts=1
                ptsjug4=ptsjug4+pts
                print("El jugador No."+ str(num_jugador)+" con la carta: "+ str(carta)+ " Puntos: "+ str(pts)+ " Acumulados: "+ str(ptsjug4))
          num_jugador=0      
          print("Juego Empatado \n")
  jugada.clear()
  pts=0
  num_jugador=0
  num_juego=num_juego+1
  ronda=ronda-1
puntos_finales.append(ptsjug1)
puntos_finales.append(ptsjug2)
puntos_finales.append(ptsjug3)
puntos_finales.append(ptsjug4)
max_pts=max(puntos_finales)
rep_pts=puntos_finales.count(max_pts)
print("Tabla de Puntos")
for pos,put in enumerate(puntos_finales):
  pos=pos+1
  print("El Jugador No."+ str(pos)+ " Total de Puntos: "+ str(put))
if rep_pts==1:
  num_jugador=puntos_finales.index(max_pts)
  num_jugador=num_jugador+1
  print("Ganador del juego es el Jugador No."+ str(num_jugador))
else:
  print("No hay un Ganador")
puntos_finales.clear()