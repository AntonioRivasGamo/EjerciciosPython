try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise ValueError
    if edad >= 18:
        print('Mayor de edad')
    else:
        print('Menor de edad')
except ValueError:
    print('Valor no valido')
except Exception as n:
    print(type(n).__name__)