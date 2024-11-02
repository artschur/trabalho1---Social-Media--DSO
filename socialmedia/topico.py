class Topico:
    def __init__(self, nome):
        self.__nome = nome
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
