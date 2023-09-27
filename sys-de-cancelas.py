from time import sleep

dtl1 = ('-=-' * 10)
dtl2 = (' ' * 6)
print(f'{dtl1}\n{dtl2}Sistema de Canelas\n{dtl1}')
print()
sleep(1)

acesso = False

while not acesso:
    placa = str(input('Qual é a sua placa: ')).upper()
    tag = str(input('Qual é o seu tag: '))

    print('FAZENDO A LEITURA......')
    sleep(1)

    if placa == 'KNO0F84' or tag == '0584':
        acesso = True
        print('Acesso liberado!')
    else:
        print('Acesso Negado!\nTente Novamente!')
