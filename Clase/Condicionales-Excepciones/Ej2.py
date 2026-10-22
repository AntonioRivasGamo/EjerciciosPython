try:
    num1 = int(input('Introduce el primer valor: '))
    num2 = int(input('Introduce el segundo valor: '))
    if num1 > num2:
        print(f"{num1} > {num2}")
    elif num2 > num1:
        print(f"{num2} > {num1}")
    else:
        print(f"{num1} = {num2}")
except ValueError:
    print("Valor incorrecto")
except Exception as n:
    print(f"Error: {type(n).__name__}")