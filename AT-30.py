num = int(input("""Dígite um número inteiro para saber se ele
é um número Par ou Ímpar:"""))
is_even = num % 2 == 0
if is_even:
    print('seu número é par')
else:
    print('seu número é ímpar')
