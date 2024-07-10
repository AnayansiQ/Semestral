def program_2():

    # Calcular elnimpuesto de un producto
    
    print('+------------------------------------------------------+')
    print("|Hacer algoritmo que calcule el impuesto de un producto|")
    print('+------------------------------------------------------+\n')
    
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = float(input("Ingrese la cantidad de productos: "))
    
    p1 = precio * cantidad
    p2 = precio * 0.10
    
    impuesto = p1 + p2
    
    print(" \nRespuesta del programa #2")
    print("=========================\n")
    
    print(f"El impuesto del producto es: {impuesto:.2f}")
    
    print("\n")
    input("Press the enter key to continue: ")