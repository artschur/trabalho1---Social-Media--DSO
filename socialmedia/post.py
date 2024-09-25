from like import Like
from comentario import Comentario
from datetime import datetime

class Post:
    def __init__(self, conteudo: str, autor):
        self.__conteudo = conteudo
        self.__likes = []  # Um post pode ter muitos likes
        self.__comentarios = []
        self.__autor = autor
        self.__data_do_post = datetime.now()

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, novo_conteudo):
        self.__conteudo = novo_conteudo

    @property
    def likes(self):
        return self.__likes

    @property
    def comentarios(self):
        return self.__comentarios

    @property
    def autor(self):
        return self.__autor
    
    @property
    def data_do_post(self):
        return self.__data_do_post

    def receber_like(self, like):
        assert isinstance(like, Like)
        self.likes.append(like)

    def adicionar_comentario(self, conteudo: str, autor):
        novo_comentario = Comentario(conteudo=conteudo, autor=autor)
        self.comentarios.append(novo_comentario)

    def deletar_comentario(self, comentario: Comentario):
        if comentario in self.__comentarios:
            self.__comentarios.remove(comentario)
            return "Comentario deletado"
        return "Comentario não encontrado"

    def count_likes(self):
        return len(self.__likes)

    def count_comentarios(self):
        return len(self.__comentarios)
    
    def relatorio_likes(self):
        return [like.usuario.username for like in self.__likes]
