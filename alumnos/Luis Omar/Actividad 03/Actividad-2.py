#act.2
num1=float(input("Ingresa el primer numero\n"))
if (num1<0):
  print("Valor incorrecto")
elif(num1>0): 
  num2=float(input("Ingresa el segundo numero\n"))
if(num2<0):
  print("Valor incorrecto")
elif(num2>0):
  num3=float(input("Ingresa el tercer numero\n"))
if(num3<0):
  print("Valor incorrecto,no se puede calcular el promedio") 
else:
  promedio=(num1+num2+num3)/3
  print("El promedio es:"+ str(promedio))