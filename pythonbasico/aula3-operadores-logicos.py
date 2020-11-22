var_verdadeiro = True #Tipo Boolean
var_falso = False

print(type(var_verdadeiro), type(var_falso))
print(var_falso)
print(var_verdadeiro)

print('\n ____________________________ \n ')

#Comparações: == != < > <= >=
# and / or / not

if var_verdadeiro == True:
    print('Var_verdadeiro é verdadeiro!')

print('\n ____________________________ \n ')

a=1
b=2

if a < b and 'abacaxi' == 'uva':
    print(a, 'é menor do que ', b)
else:
    print(a, 'não é menor do que ', b)

print('\n ____________________________ \n ')

print(not True)

idade = 50

if not idade == 50:
    print('Você não tem 50 anos')
else:
    print('Você tem 50 anos')

print('\n ____________________________ \n ')

print('Opcoes: \n 1 = Escreve Pamela \n 2 = escreve Joao '
      '\n 3 = escreve Maria')
opcao = input('Escolha uma opcao: ')

if opcao == '1':
    print('Pamela')
elif opcao == '2':
    print('Joao')
elif opcao == '3':
    print('Maria')
else:
    print('Escola uma das opções validas')

'''
Exercicio: Faça um programa que pergunte a idade, o peso e a altura de
uma pessoa e decide se ela esta apta a ser do Exercito
para entrar no Exercito é preciso ter mais de 18 anos e
pesar mais ou igual de 60 kilos e medir mais ou igual de 1,70 metros
'''