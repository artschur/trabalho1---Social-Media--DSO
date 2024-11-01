class Topico:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__posts = []
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def posts(self):
        return self.__posts
    
    def adicionar_post(self, post):
        self.__posts.append(post)
        