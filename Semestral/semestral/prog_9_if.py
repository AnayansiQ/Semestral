def program_18():

    # Sentencia if, elif, else
    # Programa 9
    
    print('+--------------------------------------------------+')
    print("|Determinar si un caracter es una letra o un digito|")
    print('+--------------------------------------------------+\n')
    
    caracter = input("Ingresa un caracter: ")
    
    print(" \nRespuesta del programa #18")
    print("==========================\n")
    
    if len(caracter) == 1: 
        
        if caracter.isalpha():
            print("El caracter ingresado es una Letra.")
            
        elif caracter.isdigit():
            print("El caracter ingresado es un Digito.")
            
    else: 
        print("El caracter ingresado no es ni una letra ni un digito.")
        
    print("\n")
    input("Press the enter key to continue: ")
    
