def program_44():

    # Bucle for
    # Programa 7 | for
    
    print('+----------------------------------+')
    print("|Dibujar un triangulo de asteriscos|")
    print('+----------------------------------+ \n')
    
    
    numero = int(input("Ingresa un numero positivo: "))
    
    print("\n")
    
    print(" \nRespuesta del programa #44")
    print("==========================\n")
    
    for i in range(1, numero + 1):
    	print("    *    " * i)
    	print()
    	
    if numero < 0: 
    	print("Intenta con un numero positivo")
    	
    print("\n")
    input("Press the enter key to continue: ")