def program_43():
    
    # Bucle for
    # Programa 6 | for
    
    print('+-------------------------------------+')
    print("|Convertir grados Celsius a Fahrenheit|")
    print('+-------------------------------------+ \n')
    
    
    ce_in= int(input("Ingresa la temperaruta en °C inicial: "))
    ce_fin = int(input("Ingresa la temperatuta en °C final: "))
    
    print("\n")
    
    print("Celsius     |      Fahrenheit")
    print("_____________________________\n")
    
    print(" \nRespuesta del programa #43")
    print("==========================\n")
    
    for temperatura in range(ce_in, ce_fin + 1): 
    	f = (temperatura * (9 // 5)) + 32
    	print(f'{temperatura} °C en fahrenheit es {f} °F')
    	
    print("\n")
    input("Press the enter key to continue: ")
