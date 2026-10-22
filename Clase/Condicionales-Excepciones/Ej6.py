try:
    print("Par" if int(input('Introduce un numero: ')) % 2 == 0 else "Impar")
except Exception as n:
    print(type(n).__name__)