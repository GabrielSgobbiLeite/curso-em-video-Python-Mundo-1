frase = input('digite seu nome?')

frase = frase.strip()

print(frase.upper())
print(frase.lower())
print(len(frase.replace(' ', '')))

nome = frase.split()[0]

print(len(nome))
