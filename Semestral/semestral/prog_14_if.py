def program_23():

    # Sentencia if, elif, else
    # Programa 14
    
    print('+-----------------------------------+')
    print("|Verificar si un triangulo es valido|")
    print('+-----------------------------------+\n')
    
    lado_1 = float(input("Ingresa la longitud del lado 1: "))
    lado_2 = float(input("Ingresa la longitud del lado 2: "))
    lado_3 = float(input("Ingresa la longitud del lado 3: "))
    
    longitud_xy = lado_1 + lado_2
     
    print(" \nRespuesta del programa #23")
    print("==========================\n")
    
    if longitud_xy > lado_3: 
        print(f"La suma de los lados 1 y 2 es {longitud_xy:.2f} y es mayor que la longitud del lado 3")
        
    else: 
        print(f"La longitud del tercer lado es mayor es mayor que {longitud_xy} que corresponde a la suma de los lados 1 y 2")
        
    print("\n")
    input("Press the enter key to continue: ")