stock = 25
on = True
while on:
    try:
        print("1.Comprar entradas\n"
              "2.Mostrar entradas disponibles\n"
              "3.Salir\n")
        match (int(input("Opción: "))):
            case 1:
                entradasAComprar = int(input("Introduce cuantas entradas quieres: "))
                if entradasAComprar < 1:
                    raise ValueError("Introduce al menos 1 entrada")
                if (stock - entradasAComprar) >= 0:
                    if entradasAComprar == 1:
                        print("Aqui tienes tu entrada")
                    else:
                        print(f"Aqui tienes tus {entradasAComprar} entradas")
                    stock -= entradasAComprar
                else:
                    print("No quedan entradas suficientes")
            case 2:
                print(f"Quedan {stock} entradas")
            case 3:
                print("Adios")
                on = False
            case _:
                "Introduce una opción valida"

    except ValueError as e:
        print(e)