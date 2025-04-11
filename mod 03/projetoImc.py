peso = float(input('Insira o seu peso: '))
altura = float(input('Insira sua altura: '))

imc = peso/(altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >=18.5 and imc <= 25:
    print('Peso normal')
else:
    print('você está acima do peso')