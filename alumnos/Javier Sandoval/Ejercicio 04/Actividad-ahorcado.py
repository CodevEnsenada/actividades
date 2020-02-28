import random

monito1 = (
 "   +---+ \n"
 "   |   |\n"
 "       |\n"  
 "       |\n"
 "       |\n"
 "       |\n"
 " =========\n")

monito2 = (
 "   +---+ \n"
 "   |   |\n"
 "   O   |\n"  
 "       |\n"
 "       |\n"
 "       |\n"
 " =========\n")

monito3 = (
 "   +---+ \n"
 "   |   |\n"
 "   O   |\n"  
 "   |   |\n"
 "       |\n"
 "       |\n"
 " =========\n")

monito4 = (
 "   +---+ \n"
 "   |   |\n"
 "   O   |\n"  
 "   |\  |\n"
 "       |\n"
 "       |\n"
 " =========\n")

monito5 = (
 "   +---+ \n"
 "   |   |\n"
 "   O   |\n"  
 "  /|\  |\n"
 "       |\n"
 "       |\n"
 " =========\n")

monito6 = (
 "   +---+ \n"
 "   |   |\n"
 "   O   |\n"  
 "  /|\  |\n"
 "    \  |\n"
 "       |\n"
 " =========\n")

monito7 = (
 "   +---+ \n"
 "   |   |\n"
 "   O   |\n"  
 "  /|\  |\n"
 "  / \  |\n"
 "       |\n"
 " =========\n")

monitos = [monito1, monito2, monito3, monito4, monito5, monito6, monito7]

ganar = "Felicidades has ganado! La palabra fue: \"{}\", tuvistes {} fallos"
acertar = "Bien la letra: \"{}\" sí se encontró"
fallar = "No está esa letra, sigue intentando"
fallos = 0
palabras = ["zapato", "mocos", "otra","juanito", "ferrocarril", "parangaracutirimicuaro", "otorrinolaringologo", "langosta", "celular", "tijeras", "zancudo", "computadora", "monitor", "lapiz", "cuaderno", "mesa", "arquitecto", "elefante", "tornamesa", "cuadrilatero", "antena", "triangulo"]
letrasAtinadas = []
letraEvaluar = ""
letraPropuesta = ""

rand = random.randint(1,len(palabras))-1
letrasFaltantes = len(palabras[rand])
print("Bienvenido, este es el juego del ahorcado. Debes ingresar las letras para intentar adivinar la palabra que se genera de forma aleatoria")
print() #este es un espacio en blanco
print("Tienes un número limitado de fallos, hasta que el mono se ahorque")
print("Cuando estes listo presiona ENTER....")
input() 
print("Iniciamos, la primera pista es que es una palabra de " + str(letrasFaltantes) + " letras, representada por los siguientes espacios en blanco: ")
print()
print(monito1)

while(letrasFaltantes != 0):
  letrasAcertadas = 0
  print()
  for letra in palabras[rand]:
    letraEvaluar = letra
    if(letraEvaluar in letrasAtinadas):
      print(letraEvaluar, end = " ")
      letrasAcertadas = letrasAcertadas + 1
    else:
      print("_", end = " ")
  print()
  print()   
  if(letrasFaltantes == letrasAcertadas):    
    print(ganar.format(palabras[rand], fallos))
    break
# De aquí hacia atrás son preparativos (setup). A partir de aquí no avanza el programa hasta que se ingrese un a letra por parte del usuario.
  letraPropuesta = input("Ingrese una letra para evaluar ")
  if(letraPropuesta in palabras[rand]):
    letrasAtinadas.append(letraPropuesta)
    print(acertar.format(letraPropuesta))
  else: 
    print(fallar)
    fallos = fallos + 1
    print(monitos[fallos])
  if (fallos == 6):
    print("Fuiste ahorcado!")
    break