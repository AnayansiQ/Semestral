def program_36():

    # Bucle while
    # Programa 7 | while
    
    print('+-------------------+')
    print("|Contador de digitos|")
    print('+-------------------+\n')
    
    numero = int(input("Ingresa un numero: "))
    
    digitos = 0
    numero_x = numero
    
    print(" \nRespuesta del programa #36")
    print("==========================\n")
    
    while numero_x != 0: 
    	numero_x //= 10
    	digitos += 1
    	print(digitos)
    	
    print(f'El numero {numero} tiene {digitos} digitos.')
    
    print("\n")
    input("Press the enter key to continue: ")