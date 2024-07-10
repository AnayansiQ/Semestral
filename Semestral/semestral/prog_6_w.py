def program_35():

    # Bucle while
    # Programa 6 | while
    
    print("+---------------+")
    print("|Validar entrada|")
    print("+---------------+ \n")
    
    n = int(input("Ingresa un numero positivo: "))
    
    print(" \nRespuesta del programa #35")
    print("==========================\n")
    
    while n < 0:
    	print("El numero no es positivo.")
    	n = int(input("Ingresa un numero positivo: "))
    	
    print(f"El numero ingresado es {n}")
    
    print("\n")
    input("Press the enter key to continue: ")