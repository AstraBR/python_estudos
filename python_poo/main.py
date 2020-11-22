#arquivo principal

from veiculo import Veiculo #de dentro do meu arquivo veiculo, importe a classe Veiculo
from carro import Carro #impotando a HEREANÇA criada a partir de veiculo
#criando um objeto
caminhao_rosa = Veiculo('rosa', 6, 'ford', 10) #tenho que passar os argumento que criamos na classe (cor, marca e roda)

print(caminhao_rosa)
print(type(caminhao_rosa)) #o tipo vai ser a classe

print("Caminhão Rosa \n")
print('Cor: ', caminhao_rosa.cor)
print('Marca: ', caminhao_rosa.marca)
print('Rodas: ', caminhao_rosa.rodas)
print('Tanque: ', caminhao_rosa.tanque, '\n') #imprimindo os valores do meu objeto

carro_azul = Carro('azul', 'bmw', 30) #novo objeto através da classe herdada de VEICULO
print("Carro Azul \n")
print('Cor: ', carro_azul.cor)
print('Marca: ', carro_azul.marca)
print('Rodas: ', carro_azul.rodas)
print('Tanque: ', carro_azul.tanque,'\n') #imprimindo os valores do meu objeto

carro_azul.abastecer(10) #add 10 litros na variavel litros atrasves do metodo que criamos na classe Veiculo
print("Tanque: ", carro_azul.tanque)
carro_azul.abastecer(70)
print("Tanque ", carro_azul.tanque)