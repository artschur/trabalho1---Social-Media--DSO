class Like:

    def __init__(self, usuario):
        self.__usuario = usuario

    @property
    def usuario(self):
        return self.__usuario
