def program_14():
    
    # Sentencia if, elif, else
    # Programa 5
    
    print('+----------------------------------------------+')
    print("|Verificar si una palabra tiene mas de 5 letras|")
    print('+----------------------------------------------+\n')
    
    Palabra = str(input("Ingresa una palabra: "))
    
    cant_palabra = len(Palabra)
    
    print(" \nRespuesta del programa #14")
    print("==========================\n")
    
    if cant_palabra > 5:
    	print("La palabra tiene mas de 5 letras") 
    
    elif cant_palabra == 5:
        print("La palabra tiene 5 letras")
    
    else:
    	print("La palabra tiene menos de 5 letras")
    	
    print("\n")
    input("Press the enter key to continue: ")