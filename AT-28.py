import random

num = random.randint(1, 10)

for x in range(1, 10):

    num1 = int(input('Escolhar um número de 1 a 10 é dígite:'))
    if num == num1:
        print('parabens você acertou o número aleatorio')
    else:
        print('você error o número aleatorio')
