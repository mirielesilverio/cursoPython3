"""
    == : equal
    != : different
    > : bigger
    < : smaller
    >= : greater equal
    <= : lesser equal
"""

height = float(input('How tall are you? '))
weight = float(input('What is your weight? '))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Under weight')
elif 18.5 <= bmi < 25:
    print('Ideal weight')
elif 25 <= bmi < 30:
    print('Overweight')
elif 30 <= bmi < 40:
    print('Obesity')
else:
    print('Severe obesity')
