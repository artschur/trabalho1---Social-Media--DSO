from socialmedia.topico import Topico
from socialmedia.modelo import Modelo
class Post(Modelo):
    def __init__(self, titulo: str, conteudo: str, autor, topico : Topico):
        super().__init__(autor)
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__likes = []
        self.__comentarios = []
        self.__topico = topico
        #talvez o datetime de criação do post

    @property
    def conteudo(self):
        return self.__conteudo

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

    @property
    def autor(self):
        return self.__autor

    def count_likes(self):
        return len(self.likes)

    def count_comentarios(self):
        return len(self.__comentarios)

    def exibir_detalhes(self):
        print(f"Título: {self.__titulo}, Conteúdo: {self.__conteudo}, Autor: {self.autor}, Tópico: {self.__topico}")

    def validar(self):
        if not self.__titulo or not self.__conteudo:
            print("Erro: Título e conteúdo são obrigatórios")
            return False    
        return True
    