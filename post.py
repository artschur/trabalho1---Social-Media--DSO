class Post:
    def __init__(self, conteudo: str, autor: Admin):
        self.__conteudo = conteudo
        self.__likes = []  # Um post pode ter muitos likes
        self.__autor = autor

    def receive_like(self, like):
        self.likes.append(like)
