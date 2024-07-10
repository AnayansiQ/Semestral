def program_26():
    
    # Sentencia if, elif, else
    # Programa 17
    
    print('+-------------------------------------------+')
    print("|Determinar el tipo de licencia de conducir.|")
    print('+-------------------------------------------+\n')
    
    Edad = float(input("Ingresa tu edad: "))
    
    print(" \nRespuesta del programa #26")
    print("==========================\n")
        
    
    if Edad <= 17:
        tipo = "Licencia de Menor"
        
    elif Edad <= 65:
        tipo = "Licencia de Adulto"
        
    else: 
        tipo = "Licencia de Adulto Mayor"
        
    print(f"De acuerdo a tu edad, tienes: {tipo}.")
    
    print("\n")
    input("Press the enter key to continue: ")