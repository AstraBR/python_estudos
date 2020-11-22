#bibliotecas do python
import requests

'''
para utilizar as requisições web
tem q abrir o terminal e instalar o pip (pip install) e importar ao res
'''
texto = None #inicializo a variável vazia
try:
    requisicao = requests.get('http://g1.com.br')
    texto = requisicao.text
    print(requisicao.text)#mostra o conteudo do site - código
except Exception as e:
        print("Requisição deu erro:", e)
print(texto)

print(requisicao)
print(type(requisicao))

print(requisicao.status_code)




