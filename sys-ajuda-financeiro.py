from time import sleep

# gráfico básico
caracteres = ("-=-" * 12)
espaco = (" " * 10)
print(f"{caracteres}\n{espaco}Sistema bancário\n{caracteres}")
sleep(1)
print(' ')

# Código para opção de depositar
depoitar = ...

# Código para a opção de sacar
sacar = ...

# Informação do salário do cliente
salario_cliente = float(input("Informe seu salário: "))

# Código de opções para o cliente
opcao = print("Digite a opção desejada:\n|[1]Depositar|\n|[2]Sacar|\n|[3]Saldo|\n|[4]Sair|")

if opcao == 1:
    pass
elif opcao == 2:
    pass
elif opcao == 3:
    print(f"Saldo atual: {salario_cliente}")
else:
    print("Opcão invalida!")
