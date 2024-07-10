def program_21():

    # Sentencias if, elif, else
    # Programa 12
    
    print('+------------------------+')
    print("|Calcular el salario neto|")
    print('+------------------------+\n')
    
    salario = float(input("Ingrese su salario bruto: $ "))
    
    print(" \nRespuesta del programa #21")
    print("==========================\n")
    
    if salario > 2000:
    	impuesto = salario * 0.2
    	salario_neto = salario - impuesto
    	print(f"El salario neto luego de aplicar el impuesto es ${salario_neto:.2f}")
    	
    else:
    	salario_neto = salario
    	print(f"El salario neto sin cobrar impuestos es ${salario:.2f}")
    	
    print("\n")
    input("Press the enter key to continue: ")