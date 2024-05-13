a = int(input('Primeiro número:'))
b = int(input('Segundo número:'))
c = int(input('terceiro número'))

# testando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# testando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'menor número é {menor}.')
print(f'maior número é {maior}.')
