class Like:

    def __init__(self, usuario, post=None, comentario=None):
        self.__usuario = usuario

    @property
    def usuario(self):
        return self.__usuario
