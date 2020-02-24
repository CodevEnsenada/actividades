#act.6
print("Programa que calcula el area de un triangulo\n")

base=float(input("Ingresar base del triangulo:\n"))
altura=float(input("Ingresar la altura del triangulo:\n"))

if(base>0 and altura>0):
  area=(base*altura)/2
  print("El area es:"+str(area))
else:
  print("Ingresa medidas validas")