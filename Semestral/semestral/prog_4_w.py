def program_33():

    # Bucle while
    # Programa 4 | while
    
    print('+------------------+')
    print("|Adivinar un numero|")
    print('+------------------+\n')
    
    import random
    
    resp_correcta = random.randint(1,10)
    
    resp_incorrecta = 0
    
    print(" \nRespuesta del programa #33")
    print("==========================\n")
    
    while resp_incorrecta != resp_correcta: 
    	num = int(input("Adivina el numero entre 1 y 10: "))
    	if num == resp_correcta: 
    		print("¡Lo has encontrado!")
    		break
    	elif num > resp_correcta: 
    		print("El numero es menor")
    	elif num < resp_correcta:
    		print("El numero es mayor")
    
    print("Fin")
    
    print("\n")
    input("Press the enter key to continue: ")