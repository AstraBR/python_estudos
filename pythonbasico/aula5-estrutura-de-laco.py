nomes = ['Pamela', 'Marcelo', 'Joao', 'Julia']
print(nomes[0])

print('\n ____________________________  \n')

for nome in nomes:
    print(nome)
#o python identifica a quantidade de itens dentro de uma coleção, por isso n coloca
# onde começa ou para o for


print('\n ____________________________  \n')

lista_de_numeros = range(5) #função que cria uma lista de numeros

print(lista_de_numeros)

for item in lista_de_numeros:
    print(item)

lista_de_numeros2 = range(5, 10, 2) #lista de numeros que vai começar do 5 ao 10 pulando de 2
# em 2
print(lista_de_numeros2)

for item2 in lista_de_numeros2:
    print(item2)

for item3 in range(0, 100, 2):
    print(item3)

print('\n ____________________________  \n')

for item4 in range(4):
    print(nomes[item4])

print('\n ____________________________  \n')

for i in range(len(nomes)):
    print((nomes[i]))
    nomes.append('Oii')
    print(nomes)

print('\n ____________________________  \n')

palavra = "Pamela Andrelo"

for letra in palavra:
    print((letra)) #imprime cada letra da string


print('\n ____________________________  \n')

i = 0
while i < 10:
    print('i ainda é menor que 10: ', i)
    i = i + 1

print('Acabou o while', i)

print('\n ____________________________________________ \n')

print('\n ____________________________  \n')

numero = 0
while True:
    print (numero)
    if numero == 20:
        break #força a parada do while
    numero += 1

print('\n ____________________________  \n')

