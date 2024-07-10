def program_5():
    
    # Area de un trapecio
    
    print('+----------------------------+')
    print("|Calcular area de un trapecio|")
    print('+----------------------------+\n')
    
    
    Base1 = float(input("Ingresa la longitud de la primera base: "))
    Base2 = float(input("Ingresa la longitud de la segunda base: "))
    Altura = float(input("Ingresa la altura del trapecio: "))
    
    Area = (Base1 + Base2) * Altura / 2
    
    print(" \nRespuesta del programa #5")
    print("=========================\n")
    
    print(f"El area de un trapecio es: {Area}")
    
    print("\n")
    input("Press the enter key to continue: ")