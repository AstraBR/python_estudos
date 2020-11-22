#HERANÇA

from veiculo import Veiculo
class Carro(Veiculo):

    def __init__(self, cor, marca, tanque): #tirei rodas
        Veiculo.__init__(self, cor, 4, marca, tanque) #atribui um valor estatico para rodas
#modifiquei os parametros, tirei as rodas e no objeto coloquei para ser sempre 4 rodas

    def abastecer(self, litros): #sobreposição (metodos com parametros diferentes
        if self.tanque + litros > 50:
            print("Erro: tanque cheio")
        else:
            self.tanque += litros
            #colocando limite de listro no tanque