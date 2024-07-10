def program_16():

    # Sentencia if, elif, else
    # Programa 7
    
    print('+-----------------------------------------------+')
    print("|Calcular el precio con descuento de un producto|")
    print('+-----------------------------------------------+\n')
    
    precio = float(input("Ingrese el precio del producto: $ "))
    
    print(" \nRespuesta del programa #16")
    print("==========================\n")
    
    if precio > 100: 
        descuento = precio * 0.1
        p_final = precio - descuento
        
        print(f"El precio del producto es ${precio:.2f} .\nSe ha realizado un descuento de ${descuento:.2f} del precio original. \nSu precio final es {p_final:.2f}")
        
    else: 
        print(f'El precio del producto es ${precio:.2f}, no se aplica descuento.')
        
    print("\n")
    input("Press the enter key to continue: ")
     