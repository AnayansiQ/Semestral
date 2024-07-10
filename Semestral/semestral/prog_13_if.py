def program_22():

    # Sentencia if, elif, else
    # Programa 13
    
    print('+--------------------------------+')
    print("|Determinar si un año es un siglo|")
    print('+--------------------------------+\n')
        
    
    año = float(input("Ingrese un año: "))
    
    print(" \nRespuesta del programa #22")
    print("==========================\n")
        
    if año % 100 == 0: 
        print("Primer año de un siglo")
        
    else: 
        print("No es el primer año de un siglo")
        
    print("\n")
    input("Press the enter key to continue: ")