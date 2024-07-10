def program_32():

    # Bucle while
    # Programa 3 | while
    
    print('+--------------------------+')
    print("|Sumar digitos de un numero|")
    print('+--------------------------+ \n')
    
    
    num = int(input("Ingresa un numero: "))
    
    suma = 0
    act_num = num
    
    print(" \nRespuesta del programa #32")
    print("==========================\n")
    
    while act_num > 0:	
    	digito = act_num % 10
    	suma += digito
    	act_num //= 10
    	print(digito)
    	
    print(f'La suma de los digitos de {num} es {suma}')
    
    print("\n")
    input("Press the enter key to continue: ")