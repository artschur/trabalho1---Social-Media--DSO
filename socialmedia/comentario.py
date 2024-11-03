from socialmedia.modelo import Modelo
class Comentario(Modelo):
    def __init__(self, conteudo: str, autor):
        super().__init__(autor)
        self.__conteudo = conteudo
        self.__likes = []
        self.__horario_postado = None

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, novo_conteudo):
        self.__conteudo = novo_conteudo

    @property
    def autor(self):
        return self.__autor

    @property
    def likes(self):
        return self.__likes

    @property
    def count_likes(self):
        return len(self.likes)
    
    def exibir_detalhes(self):
        print(f"Conteúdo: {self.__conteudo}, Autor: {self.autor}")

    def validar(self):
        if not self.__conteudo:
            print("Erro: Conteúdo do comentário é obrigatório.")
            return False
        return True 
    
