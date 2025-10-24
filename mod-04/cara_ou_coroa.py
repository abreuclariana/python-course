import random

cara_ou_coroa = random.randint(1, 10)
print(cara_ou_coroa)

if cara_ou_coroa == 0:
    print('Cara')
else:
    print('Coroa')