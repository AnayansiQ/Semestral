def program_30():

    # Bucle while
    # Programa 1 | while
    
    print('+---------------------------------------+')
    print("|Bucle while: Sumar numeros del 1 al 100|")
    print('+---------------------------------------+')
    
    #Se crea una variable con un valor inicializado
    
    contador = 0
    suma = 0
    
    while contador <= 100:
          suma += contador
          contador += 1
          print(contador)
    
    print(" \nRespuesta del programa #30")
    print("==========================\n")
    
    print(f'La suma de estos numeros del 1 al 100 es {suma}')
    
    print("\n")
    input("Press the enter key to continue: ")
      