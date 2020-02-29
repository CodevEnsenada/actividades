import random
intentos = 1
numero = random.randrange(1, 101)
adivina = 0
#print (numero)
 
print("Hola, este es un juego en donde tratas de adivinar un número entre 1 y 100")

while (adivina != numero):
  adivina = int(input("Dame un número: "))
  if adivina == numero:
    print ("Atinaste el número en " + str(intentos) + " intentos!")

  elif adivina < numero:
    print ("Tu número está por debajo")
    intentos = intentos + 1
  else:
    print ("Tu número está por arriba")
    intentos = intentos + 1