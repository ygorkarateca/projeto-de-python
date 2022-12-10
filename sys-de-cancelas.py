from time import sleep

print('---------- Sys_Cancelas ----------')
print()

placa = str(input('Qual é a sua placa:')).upper()
tag = str(input('Qual é o seu tag: '))
print('FAZENDO A LEITURA......')
sleep(3)

if placa == 'KNO0F84':
  print('Acesso liberado!')
else:
  if tag == '0784':
    print('Acesso Liberado!')
  else:
    print('Acesso Negado!')