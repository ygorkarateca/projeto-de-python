from time import sleep
from prettytable import PrettyTable as pt
import os

# gráfico básico
minha_tabela = pt(["-", "Saldo", "Depositar", "Sacar", "Sair"])
minha_tabela.add_row(["Opções", "1", "2", "3", "4"])
print(minha_tabela)
opcao = input("Escolha opção desejada: ")
sleep(1)
print()

# Limpa o terminal
os.system('cls')

# Informação do salário do cliente
salario_cliente = float(input("Informe seu salário: "))


while opcao >= 3:

        # Opção de visualizar o saldo
        if opcao == 1:
            print(f"Saldo atual: {salario_cliente}")

        # Opção de deposito
        elif opcao == 2:
            depoitar_dinheiro = salario_cliente + ...

        # Opção de saque
        elif opcao == 3:
            sacar_dinheiro = salario_cliente - ...
            
        # Opção de sair
        else:
            print("Saindo...")
else:
    print("Operação Encerrada \nVolte sempre!")
