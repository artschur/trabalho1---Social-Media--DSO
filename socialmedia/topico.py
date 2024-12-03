from uuid import uuid4

class Topico:
    def __init__(self, nome):
        self.__id = uuid4().hex
        self.__nome = nome


    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
