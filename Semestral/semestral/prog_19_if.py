def program_28():

    # Sentencia if, elif, else
    # Programa 19
    
    print('+------------------------------------------------+')
    print("|Verificar si un nombre es corto, mediano o largo|")
    print('+------------------------------------------------+ \n')
    
    Nombre = str(input("Ingresa tu nombre: "))
    
    cant_letras = len(Nombre)
    
    print(" \nRespuesta del programa #28")
    print("==========================\n")
        
    if cant_letras <= 5: 
        print("El nombre es corto")
        
    elif cant_letras > 5 and cant_letras <= 8:  
        print("El nombre es mediano")
        
    else: 
        print("El nombre el largo")
        
    print("\n")
    input("Press the enter key to continue: ")