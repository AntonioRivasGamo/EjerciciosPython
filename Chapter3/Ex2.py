hours = 0
rate = 0
while True:
    try:
        hours = int(input('Enter hours: '))
        break
    except:
        print('Enter a valid number for hours.')
while True:
    try:
        rate = float(input('Enter rate: '))
        break
    except:
        print('Enter a valid number for rate.')

print(hours * rate)