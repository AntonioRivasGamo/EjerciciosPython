class EdadNegativa(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise EdadNegativa('La edad no puede ser negativa')
    if edad >= 18:
        print('Mayor de edad')
    else:
        print('Menor de edad')
except ValueError as e:
    print(e)
except EdadNegativa as e:
    print(e)
except Exception as n:
    print(type(n).__name__)