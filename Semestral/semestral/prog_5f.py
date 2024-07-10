def program_42():

    # Bucle for
    # programa 5 | for
    
    print('+--------------------------------------+')
    print("|Sumar los primeros N numeros naturales|")
    print('+--------------------------------------+ \n')
    
    numero = int(input("Ingresa un numero: "))
    
    print("\n")
    
    suma = 0
    
    print(" \nRespuesta del programa #42")
    print("==========================\n")
    
    for i in range(1, numero):
    	print(i)
    	suma += i
    	
    print(f"El numero ingresado es {numero}")
    print(f"La suma de los numeros que le preceden es {suma}")
    
    print("\n")
    input("Press the enter key to continue: ")