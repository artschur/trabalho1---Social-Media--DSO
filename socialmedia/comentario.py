from socialmedia.modelo import ComentarioAbstract
from uuid import uuid4

class Comentario(ComentarioAbstract):
    def __init__(self, conteudo, autor):
        super().__init__(conteudo=conteudo, autor=autor)
        self.__id = uuid4().hex

    @property
    def id(self):
        return self.__id

    @property
    def autor(self):
        return self._ComentarioAbstract__autor
    @property
    def conteudo(self):
        # Access the private variable from the parent class
        return self._ComentarioAbstract__conteudo

    @conteudo.setter
    def conteudo(self, novo_conteudo):
        if not isinstance(novo_conteudo, str):
            raise TypeError("Conteudo must be a string")
        if not novo_conteudo.strip():
            raise ValueError("Conteudo cannot be empty")
        self._ComentarioAbstract__conteudo = novo_conteudo

    @property
    def likes(self):
        return self._ComentarioAbstract__likes

    @property
    def count_likes(self):
        return len(self.likes)