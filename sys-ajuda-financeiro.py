from time import sleep
from prettytable import PrettyTable as pt
import os


# Informação do salário do cliente
salario_cliente = float(input("Informe seu salário: "))


# Limpa o terminal
os.system('cls')

# gráfico básico
minha_tabela = pt(["-", "Saldo", "Depositar", "Sacar", "Sair"])
minha_tabela.add_row(["Opções", "1", "2", "3", "4"])
print(minha_tabela)
opcao = input("Escolha opção desejada: ")
sleep(1)
print()

# Limpa o terminal
os.system('cls')

# Opção de visualizar o saldo
if opcao == "1":
    print(f"Saldo atual: {salario_cliente}")

# Opção de Depositar
elif opcao == "2":
   depositar = float(input("Qual valor para o deposito? "))
   print(f"Você depositou: R${depositar}\nSaldo atual: R${salario_cliente + depositar}")

# Opção de Sacar
elif opcao == "3":
   sacar = float(input("Qual valor do saque? "))
   print(f"Você sacou: R${sacar}\nSaldo atual: R${salario_cliente - sacar}")

# Opção de sair
else:
    print("Você saiu!")
