
while True:
    numero1 = float(input("Indica el primer número: "));
    operacion = input("Indica el operador (+, -, *, /): ");
    numero2 = float(input("Indica el segundo número: "));

    if (operacion == '+'):
        resultado = numero1 + numero2;

    elif (operacion == '-'):
        resultado = numero1 - numero2;

    elif (operacion == '*'):
        resultado = numero1 * numero2;

    elif (operacion == '/'):
        resltado = numero1 / numero2;
    else : 
        print("Operacion no válida");

    print(f"El resultado de tu operación es: {resultado}");

    pregunta = input("¿Quieres hacer otra operación? (s/n)");

    if (pregunta != 's'):
        print("ADIOS!")
        break;