def program_20():
    
    # Bucle for
    # Programa 0 | for
    
    print('+-------------------------------------+')
    print("|Bucle for: Sumar numeros del 1 al 100|")
    print('+-------------------------------------+ \n')
    
    limite = 100
    suma = 0
    
    print(" \nRespuesta del programa #20")
    print("==========================\n")
    
    for i in range(1, limite + 1):
        suma += i
        print(i)
        
    print(f"La suma de estos numeros del 1 al 100 es: {suma}")
    
    print("\n")
    input("Press the enter key to continue: ")