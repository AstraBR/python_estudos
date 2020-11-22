'''
Exercicio: Faça um programa que pergunte a idade, o peso e a altura de
uma pessoa e decide se ela esta apta a ser do Exercito
para entrar no Exercito é preciso ter mais de 18 anos e
pesar mais ou igual de 60 kilos e medir mais ou igual de 1,70 metros
'''

idade = input('Informe sua idade: ')
peso = input('Informe seu peso: ')
altura = input('Informe sua altura')

if idade > '18' and peso >= '60' and altura >= '1.70':
    print("Esta apto a entrar no Exercito")
else:
    print("Não esta apto a entrar no Exercito")
