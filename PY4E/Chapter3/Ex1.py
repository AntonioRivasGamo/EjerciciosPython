hours = int(input('Enter hours: '))
rate = float(input('Enter rate: '))

if hours > 40:
    rest = hours - 40
    normal = hours - rest
    total = normal * rate + rest * 1.5 * rate
    print(total)
else:
    print(hours * rate)