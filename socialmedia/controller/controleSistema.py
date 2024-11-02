from socialmedia.controller.controleUsario import ControleUsuario
from socialmedia.controller.controlePost import ControlePost
from socialmedia.admin import Admin
from socialmedia.post import Post
from socialmedia.topico import Topico


class ControleSistema:
    def __init__(self) -> None:
        self.__controleUsuario = ControleUsuario(self)
        self.__controlePost = ControlePost(self)
        self.__usuarioLogado = None

    @property
    def controleUsuario(self):
        return self.__controleUsuario

    @property
    def usuarioLogado(self):
        return self.__usuarioLogado

    @usuarioLogado.setter
    def usuarioLogado(self, user):
        self.__usuarioLogado = user

    @property
    def controlePost(self):
        return self.__controlePost


if __name__ == "__main__":
    sis = ControleSistema()
    user = sis.controleUsuario.tela_inicial()
    sis.usuarioLogado = user["user"]
    print(user)
    sis.controlePost.posts.append(Post("titulo", "conteudo", sis.usuarioLogado, Topico("Economia")))
    sis.controlePost.listar_posts()


