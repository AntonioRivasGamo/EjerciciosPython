class NumeroNegativo(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    primo = int(input("Introduce el número: "))
    if primo < 0:
        raise NumeroNegativo
    esPrimo = True
    for i in range(2, int(primo / 2) + 1):
        if primo % i == 0:
            esPrimo = False
            break
    print("Es primo" if esPrimo else "No es primo")
except Exception as e:
    print(e)