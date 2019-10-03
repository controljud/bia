class Bio:
    def nascer(self, nome):
        #Dados Gerais
        self.nome = nome

        #Movimentação
        self.eixo_x = 0
        self.eixo_y = 0
        
        #Características
        self.peso = 0
        self.tamanho = 0

        #Situação
        self.fome = 0

    def imprimir(self):
        print (self.nome)