cidade = input('dígite o nome da sua cidade:')


cidade = cidade.strip()
cidade = cidade.split()[0]

print(cidade == 'santo' or cidade == 'santos')
