def program_19():

    # Sentencia if, elif, else
    # Programa 10
    
    print('+--------------------+')
    print("|Comparar dos numeros|")
    print('+--------------------+\n')
    
    num_1 = float(input("Ingresa el primer numero:  "))
    num_2 = float(input("Ingresa el segundo numero: "))
    
    print(" \nRespuesta del programa #19")
    print("==========================\n")
        
    if num_1 > num_2: 
        num_mayor = num_1
        print("El primer numero es mayor")
        
    elif num_1 == num_2:
        print("Ambos numeros son iguales")
        
    else: 
        num_mayor = num_1
        print("El segundo numero es mayor")
        
    print("\n")
    input("Press the enter key to continue: ")