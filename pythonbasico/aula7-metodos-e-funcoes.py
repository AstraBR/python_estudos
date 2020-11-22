print('Função de imprimir valores ...')

len('Funcao que conta quantos itens tem no objeto')

print('\n_________________\n')

print('Criando nossa função \n')

def soma(numero1, numero2):
#def - define a função
   resp = numero1 + numero2
   return resp


retorno = soma(2,4)
print(retorno)

retorno2 = soma(12.32, 43.5)
print(retorno2)

print('\n _____________________  \n')

def imprime_oi():
    print('oi')

imprime_oi()
#n precisa ter parametro e nem return

print('\n _________________________ \n')


def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

print(tem_sete_itens("Oi pessoal"))
#posso colocar condicionais, laço de repetição ou qualquer coisa dentro das minhas funções

if tem_sete_itens('1234567'):
    print('realmente tem 7 itens')

if tem_sete_itens([1,2,3,4,5,6,7]): #posso passar coleções tbm, como no caso é uma lista
    print(True)


