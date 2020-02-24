cal = int( input("Calificacion: ") )

if cal < 4 :
  print("Estas reprobado")
elif cal > 4 and cal < 8 :
  print("pasate")
else:
  print("eres un genio")


cal1 = int(input("Dame calificacion 1:"))
cal2 = int(input("Dame calificacion 3:"))
cal3 = int(input("Dame calificacion 3:"))

promedio = (cal1+cal2+cal3)/3
print("El promedio es: ", promedio)


parono = int(input("Dame un numero: "))
resu = parono%2

if resu == 0:
  print("Tu numero es par")
else:
  print("Tu numero es impar")


for i in range(1,100+1):
  r = i%2
  if r == 0:
    print("Tu numero es par", i)
  else:
    print("Tu numero es impar", i)


