def program_15():

    # Sentencia if, elif, else
    # Programa 6
    
    print('+-------------------------------+')
    print("|Clasificar la categoria de edad|")
    print('+-------------------------------+\n')
    
    Edad = int(input("Ingresa tu edad: "))
    
    print(" \nRespuesta del programa #15")
    print("==========================\n")
    
    if Edad >= 0 and Edad <= 12: 
        categoria = "Infantil"
        
    elif Edad >= 13 and Edad <= 19:
    	categoria = "Adolescente"
    	
    elif Edad >= 20 and Edad <= 59:
    	categoria = "Adulto" 
    	
    else: 
         categoria = "Adulto Mayor"
         
    print(f"De acuerdo a tu edad, estas dentro del rango {categoria}.")
    
    print("\n")
    input("Press the enter key to continue: ")