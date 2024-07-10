def program_6():

    # Volumen de un prisma
    
    print('+---------------------------------------+')
    print("|Hallar volumen de un prisma rectangular|")
    print('+--------------------------------+++----+\n')
    
    Largo = float(input("Ingrese la longitud del prisma: "))
    Ancho = float(input("Ingrese el ancho del prisma: "))
    Altura = float(input("Ingrese la altura del prisma: "))
    
    Volumen = Largo * Ancho * Altura
    
    print(" \nRespuesta del programa #6")
    print("=========================\n")
    
    print(f"El volumen del prisma rectangular es: {Volumen:.2f}")
    
    print("\n")
    input("Press the enter key to continue: ")