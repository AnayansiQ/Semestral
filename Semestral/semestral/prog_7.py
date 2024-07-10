def program_7():

    # Resolución de ecuaciones
    
    print('+----------------------------------+')
    print("|Resolver las siguientes ecuaciones|")
    print('+----------------------------------+\n')
    
    x = float(input("Ingrese el valor de x: "))
    
    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) - 5 + (8 * x) + 2
    E = ((5 * x) + 78) / 28
    F = (((6 * x)- 7) / 4) + (((3 * x) - 5) / 7)
    
    print(" \nRespuesta del programa #7")
    print("=========================\n")
    
    print(f"El resultado de A es: {A}")
    print(f"El resultado de B es: {B}")
    print(f"El resultado de C es: {C}")
    print(f"El resultado de D es: {D}")
    print(f"El resultado de E es: {E:.2f}")
    print(f"El resultado de F es: {F:.2f}")
    
    print("\n")
    input("Press the enter key to continue: ")