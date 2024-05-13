salario = float(input('Digite o valor do seu salario para o reajuste:'))

valor_do_reajuste_maximo = (salario * 25 / 100)
valor_do_reajuste_minimo = (salario * 15 / 100)

if salario <= 1250:
    novo_salario = valor_do_reajuste_maximo + salario
    print(f'valor do seu novo salario {novo_salario}')

else:
    novo_salario = valor_do_reajuste_minimo + salario
    print(f'valor do seu novo salario {novo_salario}')
