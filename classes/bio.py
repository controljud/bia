from random import randint
class Bio:
    def nascer(self, nome):
        #Dados Gerais
        self.nome = nome

        #Movimentação
        self.eixo_x = 0
        self.eixo_y = 0
        self.velocidade = 1

        #Características
        self.peso = 0
        self.tamanho = 0

        #Situação
        self.fome = 20

    def posicaoInicialAleatoria(self, coordenadas):
        return ''

    def posicaoInicialNascimento(self, coordenada):
        return ''

    def imprimir(self):
        print (self.nome)