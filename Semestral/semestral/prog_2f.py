def program_39():
    
    # Bucle for
    # Programa 2 | for
    
    print('+----------------------------+')
    print("|Contar vocales en una cadena|")
    print('+----------------------------+ \n')
    
    palabra = input("Ingresa un texto: ")
    
    print("\n")
    
    vocales = "AEIOUaeiou"
    
    contador = 0
    
    print(" \nRespuesta del programa #39")
    print("==========================\n")
    
    for char in palabra: 
    	if char in vocales: 
    		contador += 1
    	print(char)
    		
    print(f'La palabra {palabra} tiene {contador} vocales')
    
    print("\n")
    input("Press the enter key to continue: ")