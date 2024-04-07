from time import sleep
from prettytable import PrettyTable as pt
import os

# Condições para o código
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

# Informação do salário do cliente
salario_cliente = float(input("Informe seu salário: "))

while True:
    # Limpa o terminal
    os.system('cls')

    # gráfico básico
    minha_tabela = pt(["-", "Saldo", "Depositar", "Sacar", "Extrato", "Sair"])
    minha_tabela.add_row(["Opções", "1", "2", "3", "4", "5"])
    print(minha_tabela)
    sleep(1)

    opcao = input("Escolha a opção desejada: ")

    if opcao == "1":
        print(f"Saldo atual: {salario_cliente:.2f}")
        input("Pressione Enter para continuar...")
    elif opcao == "2":
        try:
            depositar = float(input("Qual valor para depósito? "))
            if depositar > 0:
                salario_cliente += depositar
                extrato += f"Depósito: R${depositar:.2f}\n"
                print(f"Você depositou: R${depositar}\nSaldo atual: R${salario_cliente:.2f}")
                input("Pressione Enter para continuar...")
            else:
                print("Operação falhou!")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
    elif opcao == "3":
        try:
            sacar = float(input("Qual valor para saque? "))
            if sacar > 0:
                if sacar <= salario_cliente:
                    if sacar <= limite:
                        if numero_saque < LIMITE_SAQUE:
                            salario_cliente -= sacar
                            extrato += f"Saque: R${sacar:.2f}\n"
                            numero_saque += 1
                            print(f"Você sacou: R${sacar}\nSaldo atual: R${salario_cliente:.2f}")
                            input("Pressione Enter para continuar...")
                        else:
                            print("Erro - Número máximo de saques excedido!")
                    else:
                        print("Erro - Limite de saque excedido!")
                else:
                    print("Erro - Saldo insuficiente!")
            else:
                print("Operação falhou!")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
    elif opcao == "4":
        print("Extrato:")
        print(extrato)
        input("Pressione Enter para continuar...")
    elif opcao == "5":
        break
    else:
        print('Opção escolhida não é válida!\nSelecione outra opção')
