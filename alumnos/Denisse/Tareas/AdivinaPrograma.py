num_usuario=0 #numero que penso el usuario
num_menor=[] #lista del rango menor
num_mayor=[] #lista del rango mayor
posNME=0 #contador del index del rango menor
posNMA=0 #contador del index del rango mayor
intentos=0 #contador numero de intentos  
num_atinado=0 #numero final atinado por el programa
resp=" " # respuesta (Y/N)
resp2=" " #respuesta (Y/N) Final
adivinar = "El numero que pensaste esta entre \"{0}\" y el \"{1}\" (y/n) : " #Pregunta de rangos
final = "El numero que pensaste es \"{0}\" (y/n) : " #Adivinar numero final

def checkRangos(r,a,b):#Funcion para generar rangos
  rango=0
  global posNME,num_menor,posNMA,num_mayor
  if r=="y":
      rango = ((a + b)/2)
      num_mayor.append(int(b))
      num_menor.append(int(rango))
      posNME+=1
      posNMA+=1
  elif r=="n":
      num_mayor.append(num_menor[-1])
      num_menor.append(num_menor[-2])
      posNME+=1
      posNMA+=1

def DefinirRango():#Funcion para definir el rango a trabajar ya se entre 1-50 o 50-100
  global intentos,adivinar,num_menor,num_mayor
  r=" "
  r=input(adivinar.format(50,100))
  intentos+=1
  if r.lower()=="y":
    num_menor.append(50)
    num_mayor.append(100)
    checkRangos(r,num_menor[0],num_mayor[0])  
  elif r.lower()=="n":
    intentos+=1
    r=input(adivinar.format(1,50))
    if r.lower()=="y":
        num_menor.append(1)
        num_mayor.append(50)
        checkRangos(r,num_menor[0],num_mayor[0])
        
def PensarNum():#Funcion para darle input al # que piense el usuario
  global num_usuario
  band=False
  print("                   JUEGO ADIVINA UN NUMERO \n")
  print("Instrucciones del Juego : \n")
  print("1.-Piensa un número entre el 1 y el 100.\n")
  print("2.-Tienes que indicarle al Ordenador si el número que pensaste esta entre los rangos que el te propone, contestadole (Y/N).\n")
  print("3.-Una vez que el ordenador le atine al número que pesaste, lo mencionara y te dira cuantas veces lo intento.\n")
  print("4.-Presiona ENTER para iniciar el Juego")
  input()
  while band!=True:
    num_usuario=input("Denisse piensa un numero entre 1 y el 100 : ")
    band=num_usuario.isnumeric()
    if band==False:
      print("Solo se aceptan numeros")
      num_usuario=0

PensarNum()
DefinirRango()
while num_usuario!=num_atinado: #cuerpo del sistema ,seguira el ciclo hasta que le atine al numero pensado por el usuario el sistema.
  if num_menor[-1]==num_menor[-2]:
     resp2=input(final.format(num_menor[posNME]))
     if resp2.lower()=="y":
        num_atinado=num_menor[posNME]
        intentos+=1
        break
     elif resp2.lower()=="n":
        resp2=input(final.format(num_mayor[posNMA]))
        num_atinado=num_mayor[posNMA]
        intentos+=1
        break
  elif num_menor[-1]!=num_menor[-2]:
    resp=input(adivinar.format(num_menor[posNME],num_mayor[posNMA]))
    resp.lower()
    intentos+=1
    checkRangos(resp,num_menor[posNME],num_mayor[posNMA])

print("********GAME OVER********")
print("El numero que pensaste es : "+str(num_atinado)+" le atine a los "+str(intentos)+" intentos")
