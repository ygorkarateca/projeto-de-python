import os
from prettytable import PrettyTable as pt
from time import sleep


def desligar_pc():


    while True:
        
        minha_tabela = pt(["-", "Desligar", "Cancelar", "Sair"])
        minha_tabela.add_row(["Opções", "1", "2", "3"])
        print(minha_tabela)

        start = str(input('Escolha a opção desejada: '))
        
        #Limpa o terminal
        os.system('cls')


        if start == "1":
            opcao_d = str(input('Você deseja fazer o desligamento em [S]egundos - [M]inutos - [H]oras? ')).upper()

            #Limpa o terminal
            os.system('cls')
            
            #Opção para definir em HORAS
            if opcao_d == "H":
                horas = int(input("Quantas horas? "))
                os.system(f"shutdown -s -t {horas * 3600}")
                print(f"Computador desligara daqui a {horas} Horas")
                sleep(2)

                #Limpa o terminal
                os.system('cls')
                

            #Opção para definir em MINUTOS
            elif opcao_d == "M":
                minutos = int(input("Quantos minutos? "))
                os.system(f"shutdown -s -t {minutos * 60}")
                print(f"Computador desligará daqui a {minutos} Minutos")
                sleep(2)

                #Limpa o terminal
                os.system('cls')


            #Opção para definir em SEGUNDOS
            elif opcao_d == "S":
                segundos = int(input("Quantos segundos? "))     
                os.system(f"shutdown -s -t {segundos}")
                print(f"Computador desligará daqui a {segundos} Segundos")
                sleep(2)

                #Limpa o terminal
                os.system('cls')


        elif start == "2":
            os.system("shutdown -a")
            print('Impedimento feito com sucesso!')
            sleep(2)

            #Limpa o terminal
            os.system('cls')


        elif start == "3":
            print("Programa Encerrado!")
            break


        elif start != "1" or "2":
            print("Digite uma opção válida!")
            sleep(3)

            #Limpa o terminal
            os.system('cls')
            continue

desligar_pc()
