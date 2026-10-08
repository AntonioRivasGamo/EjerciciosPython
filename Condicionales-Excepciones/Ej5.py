try:
    match (input('1. Ver perfil\n2. Editar perfil\n3. Salir')):
        case '1':
            print('Perfil')
        case '2':
            print('Editar perfil')
        case '3':
            print('Salir')
        case _:
            raise ValueError
except ValueError:
    print('Opcion incorrecta')
except Exception as n:
    print(type(n).__name__)