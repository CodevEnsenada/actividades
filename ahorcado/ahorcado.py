import random

ganar = "Felicidades has ganado la palabra fue: \"{}\", tuvistes {} fallos"
acertar = "Bien la letra: \"{}\" si se encontro"
fallar = "Sigue intentandolo"
intentos = 0
palabras = ["zapato", "mocos", "otra","juanito", "ferrocarril", "parangacutirimicuaro", "otorrinolaringologo"]
letrasAtinadas = []
letraEvaluar = ""
letraPropuesta = ""


rand = random.randint(1,len(palabras))-1
letrasFaltantes = len(palabras[rand])
print("Bienvenido este es un juego del ahorcado, usted debe ingresar las letras para intentar adivinar la palabra que se genera de forma aleatoria")
print()
print("No te preocupes, tienes todos los intentos que gustes")
print("Cuando estes listo presina ENTER para iniciar....")
input()

print("Iniciamos, la primera pista es que es una palabra de " + str(letrasFaltantes) + " letras. Representada por los asteriscos de acontinuación: ")

while(letrasFaltantes != 0):
  letrasAcertadas = 0
  print()
  for letra in palabras[rand]:
    letraEvaluar = letra
    if(letraEvaluar in letrasAtinadas):
      print(letraEvaluar, end = " ")
      letrasAcertadas = letrasAcertadas + 1
    else:
      print("*", end = " ")
  print()
  print()   
  if(letrasFaltantes == letrasAcertadas):    
    print(ganar.format(palabras[rand], intentos))
    break
  letraPropuesta = input("¿Ingrese una letra para evaluar? ")
  if(letraPropuesta in palabras[rand]):
    letrasAtinadas.append(letraPropuesta)
    print(acertar.format(letraPropuesta))
  else: 
    print(fallar)
    intentos = intentos + 1