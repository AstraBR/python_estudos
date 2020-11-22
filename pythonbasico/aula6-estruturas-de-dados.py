minha_lista = ['Pam', 'Joao'] #lista
#podemos adicionar, modificar ou excluir uma lista, 1 item por vez

minha_tupla = ('Pamela', 'Joao') #Tupla (tuple)
#ela ñ é modificavel como a lista diretamente, n consigo modificar o tamanho da minha lista

meu_dicionario = {'nome': 'Pamela', 'idade': 26} # Chave e um valor, chave a palavra e valor o significado
#dict no python, dinâmico como a lista

meu_conjunto = {'Pamela', 'Joao'} #n existe itens repetidos, se eu add item repetido apenas n adiciona
#é dinâmico, posso add ou modificar itens como a lista
#conjunto ñ é ordenado, não tem um indice
#set no python

print(minha_tupla,'\n')
print(type(minha_tupla) , '\n')
print(minha_tupla[1], '\n') #imprimo o item por indice


for nome in minha_tupla:
    print(nome)

minha_tupla = ('Joao', 'Fabricio') #substituo o valor da tupla inteira, não consigo modificar apenas 1 item
print(minha_tupla)

if 'Joao' in minha_tupla:
    print('Joao esta na coleção')
    #procura o item na coleção, pode ser lista, tupla ou conjunto


print('\n_____________________ \n')

print(meu_dicionario, '\n')

print(meu_dicionario['nome'], '\n') #verifica apenas o dado de uma chave especifica
print(len(meu_dicionario)) #posso usar o len em qualquer tipo de coleção para saber o tamanho

if 'Pamela' in meu_dicionario.values():
    print('Pamela esta no dicionário')
    #procura valores especificos dentro do dicionario


for valores in meu_dicionario.values():
    print(valores)
#imprime os valores das chaves

for chaves in meu_dicionario.keys():
    print(chaves)
#imprime as chaves do dicionario

meu_dicionario['nome'] = 'Patricia'
print(meu_dicionario, '\n')
#para alterar qualquer valor, me referencio a chave q quero alterar e depois da virgula eu colo o valor que quero q fique


meu_dicionario['endereco'] = 'Av uniao'
#adicionando uma nova chave com seu valor
print(meu_dicionario, '\n')

print('\n__________________________\n')

print(meu_conjunto) #n tem indice
meu_conjunto.add('maria') #add item no conjunto
meu_conjunto.add('Pamela') #n add itens repetidos

if 'Joao' in meu_conjunto:
    print("Foi encontrado no meu conjunto")

#a busca de dados no conjunto é muito mais rapido do q na lista
#no dicionário a procura do dado é rapida tbm

meu_conjunto.remove('Joao') #remove 1 item
print(meu_conjunto)

print('\n________________________\n')

#inicializar minhas coleções vazias

lista = []
tupla = ()
dicionario = {}
conjunto = set()


loucura = [(1,2), (3,4), (5,6), ({'joao', 'maria'}, {'gabriel'})]
#posso misturar os tipos de dados
print(loucura)
print(type(loucura))