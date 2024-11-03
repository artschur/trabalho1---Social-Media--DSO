from socialmedia.controller.controleUsario import ControleUsuario
from socialmedia.controller.controlePost import ControlePost
from socialmedia.admin import Admin
from socialmedia.post import Post
from socialmedia.topico import Topico
from socialmedia.controller.controleTopicos import ControleTopico


class ControleSistema:
    def __init__(self) -> None:
        self.__controleUsuario = ControleUsuario(self)
        self.__controleTopico = ControleTopico(self)
        self.__controlePost = ControlePost(self, self.controleTopico)
        self.__usuarioLogado = None
        self.__topico_atual = None

    @property
    def controleUsuario(self):
        return self.__controleUsuario

    @property
    def usuarioLogado(self):
        return self.__usuarioLogado

    @property
    def controleTopico(self):
        return self.__controleTopico

    @property
    def topico_atual(self):
        return self.__topico_atual

    @topico_atual.setter
    def topico_atual(self, topico):
        self.__topico_atual = topico

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
    sis.controlePost.posts.append(Post("titulo", "conteudo", sis.usuarioLogado, Topico("Economia")))
    sis.controlePost.posts.append(Post("Tec", "conteudo", sis.usuarioLogado, Topico("Tecnologia")))
    sis.controleTopico.get_topico()
    sis.controlePost.listar_posts(sis.topico_atual)



