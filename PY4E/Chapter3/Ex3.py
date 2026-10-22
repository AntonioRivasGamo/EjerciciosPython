from turtledemo.paint import switchupdown

score = 0
grade = 0
try:
    score = input('Enter grade: ')
    if float(score) < 0 or float(score) > 1:
        raise ValueError
    match float(score):
        case x if x < 0.6:
            grade = 'F'
        case x if 0.7 > x >= 0.6:
            grade = 'D'
        case x if 0.8 > x >= 0.7:
            grade = 'C'
        case x if 0.9 > x >= 0.8:
            grade = 'B'
        case x if x >= 0.9:
            grade = 'A'
except:
    grade = 'Bad Score'

print(f'Score: {score}, Grade: {grade}')