from post import Post
from like import Like
from topico import Topico


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

    def comentar(self, conteudo_comentario: str, post: "Post"):
        post.adicionar_comentario(conteudo_comentario, autor=self)

    def curtir_post(self, post: "Post"):
        post.receber_like(Like(usuario=self))

    def curtir_comentario(self, comentario):  # isso vai ter que ir pro mvc depois.
        comentario.receber_like(Like(usuario=self))


arthur = Usuario("arthur", "art@gmail.com", "123")
print(arthur.username)


p = Post("oi", arthur)

arthur.comentar("oi", p)
print(p.comentarios[0].autor.username)
print(p.comentarios[0].conteudo)  # comment ok, user ok, post ok,
tec = Topico("tecnologia")
tec.adicionar_post(p)
print(tec.posts)  # topico ok
arthur.curtir_post(p)

print(len(p.likes))  # like ok
