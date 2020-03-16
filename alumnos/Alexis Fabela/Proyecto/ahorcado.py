import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
palabras = 'valoracion dinero rojo guapo comida gordo mortal kombat web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco voleibol anillo estrella esternocelidomastoideo parangaricutirimicuaro'.split()
def PalabraAleat(listaPalabras):

    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]
def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabra):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabra)
    for i in range(len(palabra)): 
      # Remplaza los espacios en blanco por la letra
        if palabra[i] in letraCorrecta:
            espacio = espacio[:i] + palabra[i] + espacio[i+1:]
    for letra in espacio:
       # Mostrará la palabra con espacios entre letras
        print (letra, fin)
    print ("")
def elijeLetra(algunaLetra):
    # Devuelve la letra que el jugador ingreso. 
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra
def empezar():

    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')
print ('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabra = PalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabra)
    # El usuairo elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabra:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabra)):
            if palabra[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡bien! La palabra  es "' + palabra)
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabra)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabra + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabra = PalabraAleat(palabras)
        else:
            break