def program_25():

    # Sentencia if, elif, else
    # Programa 16
    
    print('+-----------------+')
    print("|Clasificar el IMC|")
    print('+-----------------+ \n')
    
    peso = float(input("Ingrese su peso: "))
    altura = float (input("Ingrese su altura: "))
    
    IMC = peso / (altura * altura)
    
    print(" \nRespuesta del programa #25")
    print("==========================\n")
    
    if IMC < 18.5:
        Clasificación = "Bajo Peso"
    
    elif IMC >= 18.5 and IMC < 24.9:
    	    Clasificación = "Normal" 
    	    
    elif IMC >= 25 and IMC < 29.9: 
            Clasificación = "Sobrepeso"
            
    else: 
            Clasificación = "Obesidad"
            
    print(f'Tienes un IMC de {IMC: .2f}, lo que indica que tu clasificacion es {Clasificación}')
    
    print("\n")
    input("Press the enter key to continue: ")