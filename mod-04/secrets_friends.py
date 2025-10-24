import random

friends = ['Clariana', 'Juliana', 'Fernanda', 'Camila', 'Aline']
secret_friend = random.choice(friends)
print(f'O amigo secreto de {secret_friend} é {random.choice(friends)}')