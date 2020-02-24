


# Ejercicio 02 - Tipo de datos, operaciones aritméticas, captura de datos.

En programación los tipos de datos son una parte fundamental de la programación en todos los lenguajes de programación que existen, los tipos de datos se utilizan para que la computadora entienda que puede y que no puede realizar con ellos un ejemplo de ello es que no puede intentar sumar una letra "A" con el numero 5. 

Entre los tipo de datos más comunes tenemos: 
-  Numeros enteros.
-  Numeros flotantes.
-  Datos booleanos (true / false).
-  Caracteres "a", "b","c".
-  Cadena de caracteres "Esta es una cadena", "anita lava la tina".

Las operaciones aritmeticas son los modificadores principales para las variables con ellas se pueden modificar el valor que se tiene. Entre lo más comunes tenemos "+", "-", "/", "\*", que corresponden a suma, resta, división y multiplicación.  
## Un poco de Python
Pyhon es un leguaje donde es muy imporante el como se manejan los margenes izquierdos de escritura, al igual que el pseudocodigo los margenes del lado izquierdo deben estar bien diferenciados para poder definir bloques de programación. **Ejemplo de programación en python:**

    a = 200  
    b = 33  
    if b > a:  
	    print("b is greater than a")  
    elif a == b:  
	    print("a and b are equal")  
    else:  
	    print("a is greater than b")
	    
El ejemplo anterior  es después de la instrucción **if** se puede notar que se tiene un espacio mayor de margen en izquierdo a partir de ese punto. Una vez se termina un bloque se regresa al tamaño del margen anterior. *Tip: Es aconsecable utilizar la tecla **Tab** en lugar de espacios del teclado para no perder la lectura*

Si tuviéramos el siguiente código nos detectaría un error debido a que no tenemos los espacios que se requieren. 

    a = 200  
    b = 33  
    if b > a:  
    print("b is greater than a")  
    elif a == b:  
    print("a and b are equal")  
    else:  
    print("a is greater than b")
    	    
## Funciones para la lección de hoy
Igualar una variable

    nuevaVariable = 3
Imprimir en pantalla

    print("Este es un texto")
Imprimir una variable

    print(nuevaVariable)
Imprimir una variable con texto

    print (str(nuevavariable) + " Cadena de texto")
Guardar un valor ingresado por el usuario

	    nombreUsuario = input("¿Cuál es tu nombre?")

Capturar un número por parte del usuario

    base = int( input("Ingresa la base del cuadrado") )
## Casting / Casteo
Al momento de capturar un valor en la pantalla es importante definir que tipo de datos es el que vamos a utilizar por default se utiliza el tipo  *cadena de carcateres* para ello tenemos una serie de funciones que nos ayudan a convertir el tipo de dato. 

    x = int(1) # x will be 1  
    y = int(2.8) # y will be 2  
    z = int("3") # z will be 3
     
    x = float(1) # x will be 1.0  
    y = float(2.8) # y will be 2.8  
    z = float("3") # z will be 3.0  
    w = float("4.2") # w will be 4.2
    
    x = str("s1") # x will be 's1'  
    y = str(2) # y will be '2'  
    z = str(3.0) # z will be '3.0'

## Actividad 01
1. En el archivo main.py que se encuentra en la raíz del proyecto escribir *print("hola mundo")* para mostrar en consola un texto de hola mundo.
2. Una vez se imprima la pantalla el *"hola mundo"* dentro de la carpeta alumnos, en la carpeta con tu nombre de alumno crear una carpeta con el nombre, *"Ejercicio 02"*
3. Dentro de la carpeta *"Ejercicio 02* crear un archivo llamado *"Actividad-1.py"*

## Actividad 02
1. En el archivo main.py que se encuentra en la raíz del proyecto agregar una variable llamada *saludo*.
2. Igualar la variable *saludo* a el texto *"Hola mi nombre es [tu nombre]"*
3. Guardar en la carpeta *"Ejercicio 02"* un archivo con el nombre *"Actividad-2.py"*

## Actividad 03
1. Generar 2 variables con nombres distintos, igualar una de las variables a "5" y la otra a "6" e imprimir el resultado de la suma de ambas variables. 
2. Guardar el archivo como *"Actividiad-3.py"*

## Actividad 04 
1. Generar 2 variables con nombres distintos, igualar una de las variables a "18" y la otra a "2".
2. Guardar el resultado de la suma de las 2 variables en una tercera variable. 
3. Imprimir el resultado de la suma de las 2 variables utiizando la tercera variable creada.
4. Guardar la actividad como *Actividad-5*

## Actividad 05
1. Imprimir en pantalla un saludo y que pregunte el nombre.
2. Pedir al usuario que ingrese su nombre. 
3. Almacenar el nombre en una variable
3. Imprimir el nombre de la persona acompañado de un *"mucho gusto"*.
4. Guardar la actividad como *Actividad-5*

## Actividad 06
- Realizar un programa que pida la base de un triangulo y la altura de un triangulo, calcule el área y lo muestre en la pantalla. Guardar la actividad como *Actividad-6.py*


