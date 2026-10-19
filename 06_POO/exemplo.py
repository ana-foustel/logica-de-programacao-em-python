#A CLASSE: O modelo( a planta)
class celular:
    def __init__(self, marca, modelo, cor, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! coloque para carregar")
        else:
            self.ligado = True
            print(f" {self.modelo} Ligado!")


#OS OBJETOS: Criados a partir da classe (as "casas")
celular1 = celular("Samsung", "GAlaxy s23", "Preto")
celular2 = celular("Motorola", "MotoG", "Azul")

#Acessando e alterando atributos
print(celular1.marca)

#Também podemos alterar diretamente
celular1.cor = "Branco"
print(celular1.cor)

#Chamando métodos
celular2.ligar()