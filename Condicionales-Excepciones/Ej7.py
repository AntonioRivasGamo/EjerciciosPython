try:
    edad = int(input('Introduce edad: '))
    match edad:
        case x if x >= 18:
            print("Coche")
        case x if x >= 16:
            print("Moto 125cc")
        case x if x >= 14:
            print("Ciclomotor")
        case x if x < 14:
            print("Ninguno")
except Exception as n:
    print(type(n).__name__)