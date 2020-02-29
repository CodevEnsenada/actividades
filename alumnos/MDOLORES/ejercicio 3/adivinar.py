## ADIVINAR EL NUMERO GENERADO POR EL PROGRAMA DE ENTRE EL 1 Y EL 15, INGRESANDO NUMEROS E IMPRIMIENDO SI ES MAYOR O MENOR EL NUMERO A ADIVINAR. MOSTRAR NUMERO DE INTENTOS.

import random

aleatorio=(random.randrange(1,15))
intento=0

##print(str(aleatorio))
adivina=int(input("Del 1 al 15, adivina el numero que estoy pensando: "))

if adivina > 15 or adivina < 1 :
  print("Valor fuera de rango, recuerda...es del 1 al 15")
  intento= intento + 1
  if adivina == aleatorio:
       print("Ganaste en el primer intento ")
  else:
    while adivina != aleatorio:
      intento= intento + 1
      if adivina > aleatorio:
        adivina=int(input("Sigue intentando, escribe un número menor: "))  
      elif adivina < aleatorio:
        adivina=int(input("Sigue intentando, escribe un número mayor: "))
    if adivina == aleatorio:
        print("Felicidades, lo lograste en " + str(intento) + " intentos")