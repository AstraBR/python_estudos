#importando bibliotecas

import sys # essa biblioteca conversa com o sistema operacional

argumentos = sys.argv #variavel da biblioteca SYS

print(argumentos) #o primeito argumento é o caminho do arquivo

def soma(n1, n2):
    return  n1 + n2

def sub (n1, n2):
    return  n1 - n2

#arg 0 - caminho do sistema operacional
#arg 1 - metodo // arg 2 - n1 // arg 3 - n2
if argumentos[1] == 'soma':
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == 'sub':
    resp = sub(float(argumentos[2]), float(argumentos[3])

