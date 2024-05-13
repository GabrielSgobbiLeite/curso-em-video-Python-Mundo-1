VIAGEM_LONGA = 0.45
VIAGEM_CURTA = 0.50

viagem = float(input('você vai fazer uma viagem de quantos kilometros:'))

if viagem <= 200:
    PC = viagem * VIAGEM_CURTA
    print(f'sua passagem vai custar {PC}R$.')
else:
    PL = viagem * VIAGEM_LONGA
    print(f'sua passagem vai custar {PL}R$.')
