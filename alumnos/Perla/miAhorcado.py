import random

palabras = ["oso", "casa", "perico", "muñeca", "asterisco", "conejo", "murcielago", "cebra", "maquillaje", "periodico", "arrabalero", "pintoresco", "meditabundo"]
error = 0
adivinadas = []
faltantes = 0
encontradas = 0
guess = ""
print()
print("¡Hola!  juguemos al ahorcado, debes adivinar la palabra oculta una letra a la vez")
print()
print("No hay límite de intentos")
print()
print("Pulsa <<ENTER>> para iniciar")
input()
palabra = palabras[(random.randint(0,len(palabras)-1))]
faltantes = len(palabra)
print("la palabra oculta tiene " + str(faltantes) + " letras")
while encontradas < faltantes:
  print()
  for letra in palabra:
    if letra in adivinadas:
      print(letra, end = " ")
    else:
      print("*", end = " ")
  print()
  print()
  guess = input("dame una letra > ")
  print()
  if guess in palabra and guess != "" and guess not in adivinadas:
   adivinadas.append(guess)
   print("correcto, si hay " + guess)
   veces = palabra.count(guess)
   encontradas = encontradas + veces
  elif guess in adivinadas:
      print("*** ya habías dicho "  + guess + " ***")
  else:
    error = error + 1  
    print("¡ups!, trata de nuevo")
  print() 
for letra in palabra:
  print(letra, end = " ")
print() 
print()
print("Felicidades, adivinaste con " + str(error) + " errores ☺")