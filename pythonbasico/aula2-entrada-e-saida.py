print('Hello World! \n  Segundo Print')
print('quebra de linha no mesmo print \n')

print('Hello World! \t  Segundo Print')
print('função tab \n _______________ \n')

print('Variáveis')

a = 10
b = 20


print(a+b)

nome = 'Pamela'
idade = 28
altura = 1.63
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)
frase = nome, 'tem', idade, 'anos e ', altura, 'de altura'

print(nome)
print(tipo_nome)
print(idade)
print(tipo_idade)
print(altura)
print(tipo_altura)

print(nome, 'tem', idade, 'anos e ', altura, 'de altura')
print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura')
print(frase, '\n ________________________ \n')

nome1 = input('Escreva seu nome: ')
print(nome1)
idade1 = input('Escreva sua idade: ')
print(idade1)
altura1 = input('Escreva sua altura: ')
print(altura1)

print('O input sempre retorna tipo str')

print(type(nome1), type(idade1), type(altura1))

numero1 = 10 #comentários
numero2 = 2
numero3 = 5.5

resultado = (numero1 + numero2) / numero3 * 5

print('Calcular raiz quadrada')
resultado2 = numero1 ** (1/2) #raiz quadrada de 10
print(resultado2)



'''
Exercicio: Faça um formulário que pergunte o nome, cpf, endereço, idade, altura e
telefone e imprima isso em um relatório organizado
'''
