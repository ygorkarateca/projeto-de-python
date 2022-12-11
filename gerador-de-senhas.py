import random

letras_grandes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_pequenas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&?"

usar = letras_grandes + letras_pequenas + numeros + simbolos
total_caracteres =  8

senha = "".join(random.sample(usar, total_caracteres))

print(f'Sua nova senha é: {senha}')
