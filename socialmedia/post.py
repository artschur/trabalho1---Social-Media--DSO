from socialmedia.topico import Topico

class Post():
    def __init__(self, titulo: str, conteudo: str, autor, topico : Topico):
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__autor = autor
        self.__likes = []
        self.__comentarios = []
        self.__topico = topico

    @property
    def conteudo(self):
        return self.__conteudo

    @property
    def autor(self):
        return self.__autor
    
    @conteudo.setter
    def conteudo(self, novo_conteudo):
        self.__conteudo = novo_conteudo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def topico(self):
        return self.__topico

    @topico.setter
    def topico(self, novo_topico):
        self.__topico = novo_topico

    @property
    def likes(self):
        return self.__likes

    @property
    def comentarios(self):
        return self.__comentarios

    def count_likes(self):
        return len(self.likes)

    def count_comentarios(self):
        return len(self.__comentarios)