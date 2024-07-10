def program_38():

    # Bucle for
    #Programa 1 | for
    
    print('+--------------------+')
    print("|Tabla de multiplicar|")
    print('+--------------------+ \n')
    
    tabla = int(input("Ingresa un numero: "))
    
    print("\n")
    
    print(" \nRespuesta del programa #38")
    print("==========================\n")
    
    print(f"Tabla de {tabla}\n")
    
    for multiplicador in range(1,11): 
        resultado = tabla * multiplicador
        print(f'{tabla} * {multiplicador} = {resultado}')
        
    print("\n")
    input("Press the enter key to continue: ")