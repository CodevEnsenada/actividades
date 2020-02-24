
# Ejercicio 03 - Condiciones y ciclos.

La programación es una replicación del entorno real y sabemos que las actividades que realizamos no la hacemos de forma secuencial siempre hay variaciones. Por ejemplo para ir al cine: "Si hay una pelicula interesante entonces ire", "Si hay agua lavare los trastes", "Si no viene el profe, me ire temprano a mi casa"

Un ejemplo en un algoritmo sería como el lo siguiente:

       Pasar a la caja de la tienda
       Esperar a que me diga el monto total a pagar
       Decir que voy a pagar con tarjeta
       Esperar la respuesta de la cajera
       	Si hay sistema:
       		Pagar con tarjeta
       		Esperar a que me pregunte si retirare efectivo
       		Comentar el monto que quiero retirar
       		Esperar el cobro
       		Si mi tarjeta tiene firma electronica:
       			Ingresar firma en el pat
       		Si no tiene firma electronica:
       			Firmar el recibo
      	Si no hay sistema:
      		Sacar mi cartera
      		Tomar monto mayor o igual al monto total a pagar
      		Si es mayor el monto:
    			Esperar el cambio y el ticket
    		Si el monto que pague es exacto
    			Tomar el ticket
    	Tomar las cosas con mis bolsas ecologicas
    	Agradecerle a la persona que guarda las cosas en las bolsas
    	Salir de la tienda 

Como se puede apreciar se tienen distintas condiciones que nos hacen tomar un camino o otro para poder llegar a un objetivo o solucionar un tema. 

Las condiciones tienen operadores al igual que las operaciones aritméticas con las cuales evaluamos si debo tomar una opción o otra, los operadores que se utilizan los siguiente.
- **Igual que:**     ==
- **Mayor o igual que:**     >=
- **Menor o igual que:**     <=
- **Menor que:**     <
- **Mayor que:** >
- **No igual:** !=

Ejemplo:

    a = 33  
    b = 200  
    if b > a:  
	    print("b Mayor que a")
	    
En el ejemplo anterior como se puede ver el margen izquierdo se debe aumentarse como en el ejemplo del algoritmo.

Cuando se realiza una "comparación" para ver si se cumple o no se cumple, nos regresara un valor "true" o "false" donde en base a si es correcto o no ejecutara lo que esta seguido del if. 
Podemos describir una secuencia condicional o de If como una oración del siguiente tipo:

*"Si esta lloviendo tomaré mi paraguas si no tomare mis lentes de sol."*

Como se puede ver se evalúa un solo caso pero se pueden dar dos posibles resultados, en este caso podemos tener un programa como el siguiente en Python.

    clima = "lluvioso"
    if (clima == "lluvioso"):
    	print ("Debo de tomar el paraguas")
    else:
    	print ("perfecto tomare mis lentes de sol")
   
  Otro ejemplo de una condicional podría ser la siguiente oración:
  
*Si hace calor me comprare un refresco si hace frío comprare un café pero si no hace ni frió ni calor comprare unas sabritas*

    temperatura = 30
    if (temperatura > 30)
    	print("hace calor me comprare un refresco")
    elif (temperatura < 12):
    	print("brrr.... hace frío creo que debo comprar un café")
    else: 
    	print("el día esta muy agradable debería de comprar unas sabritas")

Para el ejemplo anterior estamos suponiendo que un clima agradable es entre los 12 y 30 grados y que fuera de ese rango ya hace calor o frío. 

Existen condiciones que abarcan múltiples criterios por ejemplo: 

*"Voy a ir al cine si hay una película interesante y sí me alcanza el dinero"*

La oración anterior se podría representar de la siguiente forma en python:

    dinero = 20
    peliculaBuena = 1 ## 1 = hay buena pelicula, 0 = no hay buena pelicula
    if(peliculaBuena == 1 and dinero >= 75):
    	print("Me alcanza y hay buena película... al cine!")
    else: 
    	print("No me alcanza no hay buena película... no hay cine")

Si tenemos el siguiente código: 

    calificacion = 8
    if  (calificacion >= 6 ):
    	print("Alumno paso la materia")
    else: 
    	print("Reprobado vas a tener que hacer extraordinario")

¿Cual sería la oración que lo pudiera representar?

## Ciclos
Un ciclo es una actividad que se repite mientras se cumple una condición; por ejemplo tomar monedas de 1 peso hasta llegar al cambio que se requiere entregar al cliente, avanzar un paso hasta llegar a la puerta, girar cierta cantidad de vueltas a un tornillo hasta sacarlo por completo, leer un texto hasta terminar de entenderlo. 

En Python podemos encontrar dos tipos de ciclos el ciclo **for** que veremos en la siguiente sesión y el **while** que lo podrías traducir *"mientras que"* en la programación. 

La estructura de while la podemos encontrar como

    while(condición):
    	...instrucciones
    instrucciones que se ejecutan cuando la condición ya no se cumple

Si volvemos al ejemplo de las condiciones  una oración que utilice este comando sería. 

*"Voy ahorrar 1 peso mientras que tenga menos de 100 pesos "*

En programación quedaría algo así. 

    dinero = 0
    while(dinero < 100):
    	dinero = dinero + 1
    	print("Tengo ahorrados: " + str(dinero))
    print("Ya tengo " + str(dinero) +  " Pesos")

**Un ciclo se utiliza para** 
-   Disminuir la cantidad de instrucciones a usar.
    
-   Reducir el tamaño del programa.
    
-   Programar con mayor rapidez.
    
-   Solicitar datos según un valor desconocido al momento de ejecutar la aplicación.

Ejemplo: 
*"Mientras este lloviendo voy a usar mi paraguas si deja de llover voy a guardar mi paraguas"*

    estaLloviendo = "si"
    while(Lloviendo != "no"): 
    	estaLloviendo = input("¿Esta lloviendo en este momento \n?")
    	if(estaLloviendo != "no"):
    		print("Hay que usar el paraguas")
    print("Que bueno que ya dejo de llover")

## Ejercicios
Los siguientes ejercicios hay que guardarlos en la carpeta con tu nombre dentro de alumnos en una carpeta llamada *Ejercicio3*
1. Pedir la calificación de un alumno y decirle si es menor que 4 esta reprobado si es menor o igual que 8 decirle que paso apenas pero si es mayor que 9 felicitarlo por su excelente trabajo. Guardar el archivo como **actividad-1** dentro de la carpeta Ejercicio3 que creaste.
2. Calcular el promedio de 3 números que se soliciten al usuario *Recuerda usar la función input y el casting de la sesión anterior*. Guardar el archivo como **actividad-2** dentro de la carpeta Ejercicio3 que creaste.
3. Pedir un número y revisar si es par o impar, mostrar en pantalla si es par o impar. Guardar el archivo como **actividad-3** dentro de la carpeta Ejercicio3 que creaste.
4. Imprimir en pantalla los número del 1 al 100.
5. Imprimir la pantalla del 1 al 100 pero si es un número par poner al lado del número la frase. *"Es par"*.
