'''
Entrada e saida de arquivos
'''

'''
open('arquivo.txt')
open('C:\\windows\\arquivo') #\\ porque a \ é um caracter especial do python então deve-se colocar o \\ para entender que é uma \

ESTA TUDO COMENTADO, NESTA CASO PQ OS ARQUIVOS N EXISTEM E DÁ ERRO NA EXCUÇÃO
'''

open('arquivo.txt', 'w') #argumento w é escrita, se o arquivo n existir, ele cria, o r ele lê e dá erro caso o arquivo n tenha sido criado
#open('arquivo.txt', 'r+') #metodo de leitura e escrita, esta cometado porque o arquivo n foi criado e da erro, pq primeiro ele tenta ler o arquivo e depois ele escreve
open('arquivo.txt', 'a') #argumento a é o metodo apendi, ele vai escrevendo no final do arquivo
'''Métodos para arquivo de texto'''

#open('arquivo.jpeg', 'b') #arquivos q n são de texto, tipo imagens ...


arquivo = open('arquivo1.txt', 'w')
type(print(arquivo))

#escrevendo no arquivo
arquivo.write('Olá Mundo')

#escrever dentro do arquivo de 0 à 999, pulando 1 linha a cada numero
for i in range (0, 1000):
    arquivo.write(('numeros: ' + str(i)+'\n')) #tem q colocar o i como str para escrever, por ser um arquivo .txt

arquivo = open('arquivo1.txt', 'r')
print(arquivo.read()) #lendo o arquivo no terminal

#lendo no terminal com o for
for linha in arquivo:
    print(linha)
