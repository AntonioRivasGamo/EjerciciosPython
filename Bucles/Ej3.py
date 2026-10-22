try:
    num = int(input("Introduce un numero: "))
    line = ""
    while num > 0:
        line += f"{num},"
        num -= 1
    line += "0"
    print(line)
except Exception as e:
    print(type(e).__name__)