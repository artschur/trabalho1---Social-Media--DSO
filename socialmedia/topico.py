class Topico:
    def __init__(self, name):
        self.__posts = []
        self.__name = name

    @property
    def posts(self):
        return self.__posts

    @property
    def name(self):
        return self.__name

    def adicionar_post(self, post):
        self.__posts.append(post)

    def devolver_topico(self, post):
        if post in self.__posts:
            return self
