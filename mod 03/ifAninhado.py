print('Bem vindo(a) a aula!')

altura = float(input('Qual a sua altura? '))
conta = 0


if altura >= 1.20:
   print('Vende o ingresso') # esse recuo do print é importante, pois indica que ele está dentro do if e else
   idade = int(input('Qual é a sua idade? '))
   if idade <= 12: # primeira condição
      conta = 5
      print('O ingresso vai custar R$ 5 reais')
   elif idade <=18: # segunda condição
      conta = 12
      print('O ingresso vai custar R$ 12 reais')
   else: 
     conta = 24
     print('O ingresso vai custar R$ 24 reais')
     photo = input('Vai quer a foto?  Sim (s), Não (n) ')
     if photo == 's':
        conta += 3
        print(f'Sua conta final é R${conta}')
else:
  print('lamento você não vai!') # CUIDADO COM A ENDENTAÇÃO!!!, CADA PRINT DENTRO DO SEU IF E ELSE

  #PODE TER VARIOS ELIF E ELSE QUE QUISER