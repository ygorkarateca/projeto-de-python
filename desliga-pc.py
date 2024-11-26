import os


while True:

    start = str(input('Deseja executar o shutdown - [S/N]: ')).upper()

    if start == "S":
        segundos = int(input('Quantos segundos? '))
        os.system(f"shutdown -s -t {segundos}")
    elif start == "N":
        os.system("shutdown -a")
    else:
        print('Digite um comando válido - [S ou N]: ')
        break

