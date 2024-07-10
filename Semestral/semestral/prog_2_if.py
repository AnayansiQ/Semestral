def program_11():

    # Sentencia if, elif, else
    # Programa 2
    
    print('+------------------------------------+')
    print("|Determinar la edad de un adolescente|")
    print("+------------------------------------+ \n")
    
    
    Edad = float(input("Ingrese la edad: "))
    
    print('\n')
    
    print(" \nRespuesta del programa #11")
    print("==========================\n")
    
    if (Edad >= 13) and (Edad < 20):
        calificación = "Adolescente"
        
    elif Edad <= 12: 
        calificación = "Niño"
        
    else:
        calificación = "Adulto"
        
        
    print(f'De acuerdo a la edad ingresada, la persona es un {calificación}')
    
    print("\n")
    input("Press the enter key to continue: ")