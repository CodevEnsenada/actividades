import random
import os
numRand=0 #Valor del numero generado x el random
numAdiv=0 #Valor que ingresa el usuario
a=0
numInt=0 #Numero de intentos
resp="Y" #Variable que indica si desea volver a jugar
while resp=="Y" or resp=="y":
  print("\nADIVINA EL NUMERO")
  numRand=random.randint(1,100)
  while numAdiv!=numRand:
    numAdiv=int(input("El numero que generaste es? : "))
    numInt=numInt+1
    if numAdiv>numRand:
      print("Tu número está por arriba")
    elif numAdiv<numRand:
      print("Tu número está por debajo")
  print("\nWOOOOO!! LO ADIVINASTE \n")
  print("El numero correcto es el : " + str(numAdiv) + "\n")
  print("Lo lograste en : " + str(numInt) + " intento(s)")
  resp=(input("Jugar otra vez (Y/N) : "))
  numRand=0
  numAdiv=0
  numInt=0
  listaInt=[]
  os.system ("clear")
print("GAME OVER")