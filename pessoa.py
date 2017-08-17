class pessoa():

    def __init__(self, nome):
        self.nome = nome

    def falar (self):
        print("falando genericamente")

    def andar (self):
        print("andando genericamente")

    def pagar (self):
        print ("pagando genericamente")

class cliente(pessoa):

    def __init__(self, nome):
        super(cliente, self).__init__(nome)

    def pagar(self):
        print("cliente pagando")

class funcionario(pessoa):
    def __init__(self, nome):
        super(funcionario, self).__init__(nome):

class maratona():
    def correr(self, pessoa):
        pessoa.andar()
        pessoa.falar()


