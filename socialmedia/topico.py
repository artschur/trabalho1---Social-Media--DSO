class Topico:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname
