from post import Post
from like import Like
from topico import Topico


class Usuario:
    def __init__(self, username: str, senha: str) -> None:
        self.__username = username
        self.__senha = senha
        self.__logged_in = False

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, newname):
        self.__username = newname

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, newsenha):
        self.__senha = newsenha

    @property
    def logged_in(self):
        return self.__logged_in

    def login(self):
        self.__logged_in = True

    def logout(self):
        self.__logged_in = False

    def comentar(self, conteudo_comentario: str, post: "Post"):
        post.adicionar_comentario(conteudo_comentario, autor=self)

    def curtir_post(self, post: "Post"):
        post.receber_like(Like(usuario=self))

    def curtir_comentario(self, comentario):  # isso vai ter que ir pro mvc depois.
        comentario.receber_like(Like(usuario=self))


arthur = Usuario("arthur", "123")
print(arthur.username)
