class Like:

    def __init__(self, usuario, post=None, comentario=None):
        self.__usuario = usuario
        self.__post = post
        self.__comentario = comentario 

        if post and comentario:
            raise ValueError("Um like só pode pertencer a um post, ou a um comentário, não os dois.")

    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def post(self):
        return self.__post
    
    @property
    def comentario(self):
        return self.__comentario
    