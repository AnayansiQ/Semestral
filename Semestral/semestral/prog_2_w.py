def program_31():

    #Bucle while
    # Programa 2 | while
    
    print('+---------------------------+')
    print("|Contar hasta un numero dado|")
    print('+---------------------------+\n')
    
    num = int(input("Ingresa un numero: "))
    
    
    suma = 1
    
    print(" \nRespuesta del programa #31")
    print("==========================\n")
        
    while num < 0: 
        print("No es un numero positivo")
        num = int(input("Ingresa un numero: "))
        print('\n')
        
    while suma <= num:
        print(suma)
        suma += 1
        
    print("\n")
    input("Press the enter key to continue: ")