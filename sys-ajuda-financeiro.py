from time import sleep
from prettytable import PrettyTable as pt
import os


# Condições para o código

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 5


# Informação do salário do cliente
salario_cliente = float(input("Informe seu salário: "))


# Limpa o terminal
os.system('cls')

# gráfico básico
minha_tabela = pt(["-", "Saldo", "Depositar", "Sacar", "Extrato", "Sair"])
minha_tabela.add_row(["Opções", "1", "2", "3", "4", "5"])
print(minha_tabela)
sleep(1)
print()


while True:

    opcao = input("Escolha opção desejada: ")
    # Limpa o terminal
    os.system('cls')

    # Opção de visualizar o saldo
    if opcao == "1":
        print(f"Saldo atual: {salario_cliente:.2f}")

    # Opção de Depositar
    elif opcao == "2":
        depositar = float(input("Qual valor para deposito? "))
        
        if valor > 0:
            saldo += valor
            print(f"Você depositou: R${depositar}\nSaldo atual: R${salario_cliente + depositar:.2f}")

        else:
            print("Operação falhou!")

    # Opção de Sacar
    elif opcao == "3":
        sacar = float(input("Qual valor do saque? "))
        print(f"Você sacou: R${sacar}\nSaldo atual: R${salario_cliente - sacar:.2f}")

    # Opção de sair
    else:
        sair_ou_nao = str(input('Você deseja sair?\nDigite [S]sim ou [N]ão: ')).lower()
        if sair_ou_nao == "s":
            print('Você saiu')
            break
else:
    print('teste')
