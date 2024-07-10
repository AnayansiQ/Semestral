def program_29():

    # Sentencia if, elif, else
    # Programa 20
    
    print('+-----------------------------+')
    print("|Calcular la tarifa de un taxi|")
    print('+-----------------------------+ \n')
    
    distancia = float(input("Ingresa la distancia recorrida en km: "))
    
    tarifa_inicial = 2.50
    tarifa_ad = 2.00
    
    print(" \nRespuesta del programa #29")
    print("==========================\n")
    
    if distancia <= 10: 
        tarifa_total = distancia * tarifa_inicial
        
    
    else: 
        tarifa_total = (10 * tarifa_inicial) + (distancia - 10) * tarifa_ad
        
    print(f"La tarifa del taxi para una distancia de {distancia} km es ${tarifa_total:.2f}")
    
    print("\n")
    input("Press the enter key to continue: ")

    