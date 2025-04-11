print('Seja bem-vindo a pizzari Tipscode!')
size = input('Qual o tamnho da pizza? (p) pequena, (m) média, (l) grande')
pepperoni = input('Deseja adicionar pepperoni? (s) sim, (n) não')
extra_cheese = input('Deseja incluir queijo? (s) sim, (n) não')

bill = 0

if size == 'p':
    bill += 15

elif size:
    bill += 20

elif size == 'l':
    bill += 25

else:
    print('Seleção de campo inválida!')

if pepperoni == 's':
    if size == 'p':
        bill += 2
    else:
        bill += 3

if extra_cheese == 's':
    bill += 1

print(f'Valor final da pizza é: ${bill}')