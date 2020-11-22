'''
Exercicio: Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa coleção
faça outra função que retorna o menor numero dessa coleção
'''


colecao = [1,43,5,6,33,54,10]
qtde = len(colecao)

i=0
resp=0
while i < qtde:
    if resp < colecao[i]:
        resp = colecao[i]
    i+=1
print(resp, '\n')

y=1
resp2=0
while y > qtde:
    if resp2 < colecao[i]:
        resp2 = colecao[i]
    y+=1
print(resp2, '\n')