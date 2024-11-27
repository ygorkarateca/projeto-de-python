def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 2

    return antecessor, sucessor

def func_3():
    print("Olá mundo!")

print(calcular_total([10, 20, 34])) # 65
print(retorna_antecessor_e_sucessor(10)) #(9, 11)
print(func_3())