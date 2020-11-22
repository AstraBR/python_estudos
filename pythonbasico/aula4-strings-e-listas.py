frase = 'Oi, tudo bem?'
lista_nomes = ['Joao', 'Maria', 'Pamela', 'Yasmin', 10, 10.2, False]
print(lista_nomes)
print('\n ____________________________ \n ')

print(frase)
print(frase[0:13:2]) #frase[de onde começa, a onde termina, pulando
# quantos caracteres] - STEP

print('\n ____________________________ \n ')

print(type(lista_nomes))

print('\n ____________________________ \n ')

print(lista_nomes)

print('\n ____________________________ \n ')

print(lista_nomes[0:6:2])

print(lista_nomes[-2]) #conta de trás para frente

lista_nomes.append('Geralda') #jogo mais nomes na lista , sempre no
# ultimo lugar

print(lista_nomes)

lista_nomes.remove(10) #remove item da lista

print(lista_nomes)

lista_nomes.insert(1, 'José') #adicionar na posição x, o item y

print(lista_nomes)

lista_nomes[0] = 'Yasmin' #trocar o item da lista

print(lista_nomes)

contador_yasmin = lista_nomes.count('Yasmin')
#pode ter itens iguais na mesma lista
#neste item o count conta quantos Yasmin tem na mesma lista

print(contador_yasmin)

lista_nomes.clear() #limpa a lista

print(lista_nomes)

print(len(frase)) #conta a qtde de caracteres
print(len(lista_nomes))

#print(lista_nomes.pop())
#pega sempre o ultimo da lista, e tira da lista

print(lista_nomes)

print(frase.lower()) #passa td pra minuscula, n é permanente, é apenas
# na excução atual

print(frase.upper())

frase_separada = frase.split(',') #transforma em lista,
# separa os itens
print(frase_separada)
print(frase_separada[0])
print(frase_separada[1])

frase_nova = frase + ' Como vai você' #concatenação
print(frase_nova)
