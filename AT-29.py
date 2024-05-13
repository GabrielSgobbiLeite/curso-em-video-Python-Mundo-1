MAX_VELOCITY = 80

km = int(input('Qual era sua velocidade maxima:'))
if km > MAX_VELOCITY:
    vkm = km-MAX_VELOCITY
    vkm1 = vkm*7
    print(f'você foi multado em {vkm1}R$.')
else:
    print('prossiga sua viagem com segurança.')
