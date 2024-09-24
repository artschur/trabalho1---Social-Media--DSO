from post import Post
from like import Like


class Usuario:
    def __init__(self, username: str, email: str, senha: str) -> None:
        self.__username = username
        self.__email = email
        self.__senha = senha
        self.__logged_in = False

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, newname):
        self.__username = newname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, newemail):
        self.__email = newemail

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

    def comentar(self, conteudo_comentario: str, post: Post):
        if post is not None:
            post.adicionar_comentario(conteudo_comentario, autor=self)
        else:
            raise ValueError("Post não existe.")
    def curtir_post(self, post: Post):
        if post is not None:
            post.receber_like(Like(usuario=self))
        else:
            raise ValueError("Post não existe.")

    def curtir_comentario(self, comentario):
        comentario.receber_like(Like(usuario=self))
