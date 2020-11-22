class Veiculo:
    #criei uma classe chamada Veiculo


    def __init__(self, cor, rodas, marca, tanque): #objeto passa ele mesmo para ele
        #método construtor, serve para eu conseguir executar o objeto
        self.cor = cor #quando eu iniciar o objeto eu vou pegar a cor e jogar dentro do self.cor (variavel temporaria)
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros): #metodo para add valor em litros
        self.tanque += litros

#HERANÇA

