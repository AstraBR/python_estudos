#Divisão por 0
try: #significa tentar, se n conseguir fazer, faça a exceção
    a = 1200 / 0
except:
    print("Não dá para fazer divisão por zero")

print('\n____________________\n')

try:
    asdasd()
except NameError: #erro especifico
    print("Vc digitou algo errado")

print('\n________________________\n')

try:
    aaaa()
except Exception as erro: #estou jogando o erro numa variavel chamada erro
    print("Aconteceu algum erro ", erro)


print('\n___________________________\n')

#sempre usar quando há possibilidade de dar erro



