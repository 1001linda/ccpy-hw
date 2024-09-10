while True:
    try:
        height, weight = input().split()
        height = float(height)
        weight = float(weight)
    except:
        exit()
    h2 = height/100
    bmi = weight / h2**2
    if bmi < 18.5:
        print('underweight')
    elif 18.5 <= bmi < 25:
        print('normal weight')
    elif 25 <= bmi < 30:
        print('overweight')
    else:
        print('obese')

