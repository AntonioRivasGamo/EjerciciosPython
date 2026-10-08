try:
    nota = float(input("Introduce la nota: "))
    calificacion = ''
    if 0 > nota or nota > 10:
        raise ValueError
    match nota:
        case x if x < 5:
            calificacion = "Suspenso"
        case x if 7 > x >= 5:
            calificacion = 'Aprobado'
        case x if 9 > x >= 7:
            calificacion = 'Notable'
        case x if 10 > x >= 9:
            calificacion = 'Sobresaliente'
    print(calificacion)
except Exception as n:
    print(type(n).__name__)