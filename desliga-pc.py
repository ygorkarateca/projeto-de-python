import os
from PrettyTable import prettytable as pt

def desligar_pc():

    while True:

        start = str(input('Deseja executar o shutdown? - [S/N]: ')).upper()

        if start == "S":
            horas = int(input('Em quantas horas você quer desligar? '))
            os.system(f"shutdown -s -t {horas * 3600}")
            print('Agendamento feito com sucesso!')

        elif start == "N":
            os.system("shutdown -a")
            print('Impedimento feito com sucesso!')

        elif start != "S" or "N":
            print('Programa Encerrado!')
            break

desligar_pc()
