from random import randint
minumero = randint(1,15) #genero mi numero
print(minumero)          #verifico mi numero
intentos = 1
numero = int(input("adivina mi número, entre 1 y 15: "))
while numero != minumero:
  if numero > minumero:
    numero = int(input("mi número es menor, inténtalo de nuevo:"))
  else:
    numero = int(input("mi número es mayor, inténtalo de nuevo:")) 
  intentos = intentos + 1
print("adivinaste! en el intento: " + str(intentos))