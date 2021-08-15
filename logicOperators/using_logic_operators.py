name = input('What is your name? ')
age = int(input('How old are you? ') or 0)

if not name:
    print('The name cannot be empty')
elif ' ' in name:
    print('Very good! You entered your full name')
elif ' ' not in name:
    print('You must enter your full name.')

if not age or age < 0:
    print('Oh no! You entered an invalid age')
