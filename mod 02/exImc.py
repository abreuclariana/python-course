#Exercício IMC

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura * altura)

novo_imc = int(imc)

print('Seu IMC é: ' + str(novo_imc)) # NÃO é possível concatenar uma string com um number, logo deve ser o usado o str para transformar number em String

#Uso do Fstring

#nesse caso utiliza o f para concatenar sem precisar transformar o identificador em uma string
print(f'Seu IMC é {novo_imc}')