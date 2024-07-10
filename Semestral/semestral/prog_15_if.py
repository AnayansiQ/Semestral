def program_24():

    # Sentencia if, elif, else
    # Programa 15
    
    print('+----------------------------------------+')
    print("|Determinar la categoría de un trabajador|")
    print('+----------------------------------------+\n')
    
    exp_años = float(input("Ingresa tus años de experiencia: "))
    
    print(" \nRespuesta del programa #24")
    print("==========================\n")
    
    if exp_años < 2: 
        categoria = "Junior"
        
    if  2 <= exp_años <= 5:
    	categoria = "Semi-senior"
    
    if exp_años > 5: 
        categoria = "Senior"
        
    print(f"De acuerdo a tus años de experiencia eres un {categoria}.")
    
    print("\n")
    input("Press the enter key to continue: ")