from time import sleep

dtl1 = ('-=-' * 10)
dtl2 = (' ' * 6)
print(f'{dtl1}\n{dtl2}Sistema de Canelas\n{dtl1}')
print()
sleep(1)


placa = str(input('Qual é a sua placa: ')).upper()
tag = str(input('Qual é o seu tag: '))
print('FAZENDO A LEITURA......')
sleep(2)

if placa == 'KNO0F84':
  print('Acesso liberado!')
else:
  if tag == '0584':
    print('Acesso Liberado!')
  else:
    print('Acesso Negado!')
