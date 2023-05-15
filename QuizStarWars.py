pergunta1 = '1)Em que ano foi lançado o primeiro filme de star wars?'

opcoes_respostas1 = ['a)1989', 'b)1988', 'c)1998', 'd)1999']

res_correta1 = 'd'

print(pergunta1)
for opcao in opcoes_respostas1:
  print(opcao)

res_usu01 = input('')

if res_usu01.lower() == res_correta1:
  print('Certa Resposta! :)')
else:
  print('Resposta Errada! :()')


  #SEGUNDA PERGUNTA

pergunta2 =  '2)Quantos filmes Tem a franquia de Star wars?'

opcoes_res2 = ['a)9', 'b)7', 'c)10', 'd)11']

res_correta2 = 'a'

print(pergunta2)
for opcao in opcoes_res2:
  print(opcao)

res_usu02 = input('')

if res_usu02.lower() == res_correta2:
  print('Certa Resposta! :)')
else:
  print('Resposta errada jovem padawan! :()')



#TERCEIRA PERGUNTA

pergunta3= '3)No final do Filme Rey aparece com seu novo sabre de luz, Qual era a cor?'

opcoes_res3 = ['a)Roxo', 'b)Amarelo', 'c)Azul', 'd)Verde']

res_correta3 = 'b'

print(pergunta3)
for opcao in opcoes_res3:
  print(opcao)

res_usu03 = input('')

if res_usu03.lower() == res_correta3:
  print('Acerto Mizeravi !')
else:
  print('Assista o Filme Novamente')  


#QUARTA PERGUNTA

pergunta4 = 'Qual era o verdadeiro nome do Darth Vader?'

opcoes_res4 = ['a)Mace Windu', 'b)Mestre yoda', 'c)Anakin Skywalker', 'd)Luke Skywalker']

res_correta4 = 'c'

print(pergunta4)
for opcao in opcoes_res4:
  print(opcao)

res_usu04 = input('')

if res_usu04.lower() == res_correta4:
  print('Voce acerto Jedi !')
else:
  print('Essa foi por pouco!')


#QUINTA PERGUNTA

pergunta5 =  '5)Onde Luke skywalker encontra os seus robos (r2-d2 e C3PO) pela primeira vez? '

opcoes_res5 = 'a)Tatooine', 'b)Estrela da Morte', 'c)No mercado de robos', 'd)Em sua nave'

res_correta5 = 'a'

print(pergunta5)
for opcao in opcoes_res5:
  print(opcao)

res_usu05 = input('')

if res_usu05.lower() == res_correta5:
  print('Voce e um Verdadeiro Jedi !')
else:
  print('Bora assistir novamento porque nao foi dessa vez!')
