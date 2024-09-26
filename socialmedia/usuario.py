from like import Like
from comentario import Comentario
from comment_manager import CommentManager

comment_handler = CommentManager()


class Usuario:
    def __init__(self, username: str, email: str, senha: str) -> None:
        self.__username = self.__validacao_username(username)
        self.__email = self.__validacao_email(email)
        self.__senha = self.__validacao_senha(senha)
        self.__logged_in = False
        self.__posts_curtidos = []

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

    @property
    def posts_curtidos(self):
        return self.__posts_curtidos

    def __validacao_email(self, email: str) -> str:
        if "@" not in email or "." not in email:
            raise ValueError("Email Inválido.")
        return email

    def __validacao_username(self, username: str) -> str:
        if len(username) < 2:
            raise ValueError("O nome do usuário deve ter pelo menos 2 caracteres.")
        return username

    def __validacao_senha(self, senha: str) -> str:
        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres")

    def login(self):
        self.__logged_in = True

    def logout(self):
        self.__logged_in = False

    def comentar(self, conteudo_comentario: str, post: "Post", comment_manager):
        try:
            novo_comentario = Comentario(conteudo=conteudo_comentario, autor=self)
            comment_handler.comentar(
                novo_comentario,
                post=post,
            )

        except ValueError as e:
            print(f"Error: {e}")

    def curtir_post(self, post: "Post"):
        if post is None:
            raise ValueError("Post Inválido.")
        if post in self.__posts_curtidos:
            raise ValueError("Você já curtiu esse post.")
        post.receber_like(Like(usuario=self))
        self.__posts_curtidos.append(post)

    def curtir_comentario(self, comentario):
        if comentario is None:
            raise ValueError("Comentário Inválido.")
        comentario.receber_like(Like(usuario=self))
