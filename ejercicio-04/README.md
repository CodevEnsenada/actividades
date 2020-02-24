
## Listas y ciclo for 
Las listas son un conjunto de datos con el mismo tipo con el cuál podemos realizar operaciones de grupo de datos, sin la necesidad de tener multiples variables. Es un tipo de dato de los más utilizados al momento de manejar, videojuegos, sumatorias y manejo de información desde una base de datos.

La estructura de la definición es la siguiente. 

    calificacionAlumno = ["8", "7", "9", "10"]

De esta forma tenemos una sola variable que es una lista pero que contiene 4 calificaciones del alumno, si nosotros queremos imprimir el primer elemento de la lista utilizariamos la siguiente forma con el print. 

    print(calificacionAlumno[0])
    
   Como se puede observar aparece nuevamente un corchete pero se inicia desde le número cero [0], por lo tanto en el ejemplo anterior si queremos imprimir el valor de 10 sería:
 

    print(calificacionAlumno[3]) 


|Método| Descripción  |
|--|--|
|append()|Agrega elementos al final de la lista|
|clear()|Elimina todos los elementos de la lista|
|copy()|Regresa una copia de la lista|
|count()|Regresa un numero con la cantidad de elementos con un valor en especifico|
|extend()|Agrega elementos de otra lista dentro de la lista|
|index()| Regresa la posición indice de el primer elemento con el valor especificado|
|insert()|Agrega un elemento de a la lista en una posición especifica|
|pop()|Elimina el elemento de la lista de una posición especifica|
|remove(x)|Quita el primer ítem de la lista cuyo valor sea x. Es un error si no existe tal ítem.
|reverse()|Ordena de forma inversa el orden de una lista|
|sort()|Ordena la lista|

Para poder recorrer los valores dentro de un arreglo e imprimir cada uno de ellos utilizamos el ciclo for con una estructura similiar. 

    calificacionAlumno = ["8", "7", "9", "10"]
    for parcial in calificacionAlumno: 
	    print(parcial)
El ciclo for tiene una estructura de la siguiente manera:

    for [variable] in [lista]:
    	instrucciones por cada valor dentro de la lista

Para revisar si existe algún dato en especifico dentro de la lista se utiliza algo como lo siguiente:

      thislist = ["apple", "banana", "cherry"]  
	  if  "apple"  in thislist:  
		  print("Yes, 'apple' is in the fruits list")
Lo anterior recorre la lista y busca si existe por lo menos un valor dentro de la lista. 

Lo siguiente nos cuenta el número de elementos dentro de la lista: 

    thislist = ["apple", "banana", "cherry"]  
    print(len(thislist))
    
 Lo siguiente agrega un ultimo elemento dentro de la lista: 

    thislist = ["apple", "banana", "cherry"]  
    thislist.append("orange")  
    print(thislist)
    
Lo siguiente incluye un valor dentro de  la lista pero en la segunda posición (1)

    thislist = ["apple", "banana", "cherry"]  
    thislist.insert(1, "orange")  
    print(thislist)
Lo siguiente elimina todos los elementos que pongamos dentro del remove

    thislist = ["apple", "banana", "cherry"]  
    thislist.remove("banana")  
    print(thislist)

Lo siguiente elimina el ultimo elemento dentro de la lista si no se define una posición dentro del pop()

    thislist = ["apple", "banana", "cherry"]  
    thislist.pop()  
    print(thislist)

Lo siguiente elimina los valores dentro de la lista 

    thislist = ["apple", "banana", "cherry"]  
    thislist.clear()  
    print(thislist)
 


