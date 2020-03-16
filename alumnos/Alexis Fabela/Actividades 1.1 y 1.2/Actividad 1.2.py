import random

intentosRealizados = 0  
número = random.randint(1, 15)

print('Bien, estoy pensando en un número entre 1 y 15.')


while intentosRealizados < 5:
  print('Intenta adivinar el numero .') 
  estimación = input()
  estimación = int(estimación)

  intentosRealizados = intentosRealizados + 1


  if estimación < número:
    print('No, el numero  intriducido es menor.') 

  if estimación > número:
    print('Y no, ya te pasaste.')

  if estimación == número:
    break

  if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Irelo, le atinaste al número en ' + intentosRealizados + ' intentos!')


if estimación != número:
     número = str(número)
     print('Nel mijo. El número era ' + número + '!Bombo bombooo!')