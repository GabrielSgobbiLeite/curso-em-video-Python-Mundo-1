import math


c1 = float(input('Digite o valor do cateto oposto:'))
c2 = float(input('digite o valor do cateto adjacente:'))

soma = math.pow(2,c1) + math.pow(2,c2)

hipotenusa = soma**(1/2)

print(f'o valor da hipotenusa do seu tringulo retangulo é {hipotenusa:.2f}')
