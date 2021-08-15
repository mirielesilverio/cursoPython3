name = 'Miriéle Silvério'
age = 20
height = 1.56
weight = 48.00
imc = weight / (height ** 2)

print(f'My name is {name} and I am {age} years old')
print(f'My weight is {weight} kilos and my BMI is {imc:.2f}')
print('My weight is {} kilos and my BMI is {:.2f}'.format(weight, imc))
