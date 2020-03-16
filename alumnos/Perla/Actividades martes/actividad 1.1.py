rango = []
inicio = 1
mitad = 50
intentos = 0
respuesta = ""
fin = 0
numero = 1
while numero <= 100:
  rango.append(numero)
  numero = numero + 1
print("Hola, juguemos a adivinar el número \n")  
print("piensa un número entre 1 y 100 y pulsa <<ENTER >>")
input()
while len(rango) > 3:
  respuesta = input("¿tu número está entre el " + str(inicio) + " y el " + str(mitad) + "? S/N ")
  print()
  if (respuesta == "s" or respuesta == "S"):
    del rango[int(len(rango) / 2): len(rango)]
  elif (respuesta == "n" or respuesta == "N"):
    del rango[0: int(len(rango) / 2)]
  else: 
    print("respuesta incorrecta, trata de nuevo \n")
    continue
  inicio = rango[0]
  final = rango[len(rango) - 1]
  medio = int(len(rango) / 2)
  mitad = rango[medio - 1]
  intentos = intentos + 1 
while fin == 0:
  if len(rango) == 3:  
    respuesta = input("¿tu número está entre el " + str(rango[0]) + " y el " + str(rango[1]) + " ? S/N ")  
    intentos = intentos + 1
    print()
    if respuesta == "n" or respuesta == "N":
      print("tu número es el " + str(rango[2]))
      print()
      fin = 1
    else:
      respuesta = input("¿tu número está entre el " + str(rango[1]) + " y el " + str(rango[2]) + " ? S/N ")
      intentos = intentos + 1
      print()
      if respuesta == "s" or respuesta == "S":
        print("tu número es " + str(rango[1]))
        print()
        fin = 1
      else:
        print("tu número es " + str(rango[0]))
        print()
        fin = 1
    print("adiviné a los " + str(intentos) + " intentos")
  else:
    if rango[0] == 99:
      rango.insert(0, (rango[0]-1))
    else:
      rango.append((rango[1]+1))
  continue