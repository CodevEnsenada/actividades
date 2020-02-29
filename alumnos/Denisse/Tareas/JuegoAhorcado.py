import random
tablaSecreta=[] #lista de asteriscos y relleno con letras
palabraRandom="" #palabra elegida de manera random
num_letras=0 #numero de letras palabraRandon
fallaste=0 #contador numero de fallas
intentos=1 #contador numero de intentos
letra_repetida=0 #contador letras repetidas palabrarandom
cont_ast=0 #contador de # de "*" en tablaSecreta
listaPalabras=["casa","sala","cocina","tocador","recamara","closets","carro","perro","gato","humano","television","mesa","sillas"] #listado de palabras
def imprimir_asteriscos(): #funcion imprimir asteriscos
  for x in tablaSecreta:
      print(x, end=" ")
print("               JUEGO DEL AHORCADO \n")
print("Intrucciones : \n") 
print("1.-Debe de ingresar las letras para adivinar la palabra que se genera de forma aleatoria\n")
print("2.-Tienes todos los intentos que gustes para adivinar la palabra \n")
print("3.-Presina ENTER para iniciar Juego")
input() #salto de renglon
palabraRandom=random.choice(listaPalabras)
num_letras=len(palabraRandom)
while cont_ast<num_letras: #rutina donde lleno la lista de *
    tablaSecreta.append("*")
    cont_ast=cont_ast+1
print("Primer pista es una palabra con " + str(num_letras) + " letras \n")
imprimir_asteriscos()
cont_ast=0
while intentos>=1:#Rutina de interesaciones
  print("\n")
  cont_ast=tablaSecreta.count("*")
  if cont_ast>0:
    letra= input("¿Ingrese una letra para evaluar? ")
    letra_repetida=palabraRandom.count(letra)
    if letra_repetida>=1:
      print("WOOO!! Adivinaste si esta la letra : " + str(letra)+"\n") 
      for x,y in enumerate(palabraRandom):
        if letra==y: 
          tablaSecreta[x]=letra
    elif letra_repetida==0:
      fallaste=fallaste+1
      print("Falla #"+ str(fallaste) +" sigue intentandolo \n")
  else:
    print("Felicidades Ganaste!!")
    print("La palabra es : "+str(palabraRandom)+" , Tuviste : "+str(fallaste)+" fallas")
    break
  intentos=intentos+1    
  imprimir_asteriscos()