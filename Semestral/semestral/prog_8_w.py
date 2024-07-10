def program_37():
    
    # Bucle while
    # Programa 8 | while
    
    print('+----------------------------+')
    print("|Simular un cajero automatico|")
    print('+----------------------------+ \n')
    
    
    PIN = 2213
    intento = 0
    limite = 3
    
    print(" \nRespuesta del programa #37")
    print("==========================\n")
    
    while intento < limite:
    	Numero = int(input("Ingresa el numero pin: "))
    	
    	if Numero == PIN: 
    		print("Contraseña ingresada con exito")
    		break
    		
    	elif Numero != PIN:
    		intento += 1
    		print("PIN incorrecto. Intentalo nuevamente")
    		
    if intento == limite:
    	print("su tarjeta ha sido bloqueada")
    	
    print("\n")
    input("Press the enter key to continue: ")	