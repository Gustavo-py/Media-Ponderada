cod = input('Digite seu codigo de aluno: ')
nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))
nota3 = float(input('Digite sua nota 3: '))

if  nota1 > nota2 and nota1 > nota3:
    media = (nota1*4+nota2*3+nota3*3)/10
  
elif nota2 > nota1 and nota2 > nota3:
    media = (nota1*3+nota2*4+nota3*3)/10

else:
    media = (nota1*3+nota2*3+nota3*4)/10
 
if media >=5:
  print(f'SUA NOTAS FORAM: \n{nota1}\n{nota2}\n{nota3} \nE sua media foi de {media:.1f} Você obteve um desempenho maior que 5.0 \n{cod.upper()} você foi APROVADO.')

if media <=5:
    print(f'infelizmente você foi REPROVADO, Sua media foi de {media} abaixo da media esperada. ')