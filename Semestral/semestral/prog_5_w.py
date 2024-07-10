def program_34():

    # Bucle while
    # Programa 5 | while
    
    print('+-------------------------------+')
    print("|Mostrar multitplos de un numero|")
    print('+-------------------------------+ \n')
    
    numero = int(input("Ingresa un numero: "))
    inicio = 1
    
    print(" \nRespuesta del programa #34")
    print("==========================\n")
     
    print(f'Tabla de {numero}\n')
    while numero > 0:
    	resultado = numero * inicio
    	print(numero , "*", inicio, "=", resultado)
    	inicio += 1
    	if inicio > 10:
    	 break
    	 
    print("\n")
    input("Press the enter key to continue: ")
	