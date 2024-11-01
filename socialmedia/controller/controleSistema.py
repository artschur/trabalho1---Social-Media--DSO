from socialmedia.controller.controleUsario import ControleUsuario
from socialmedia.controller.controlePost import ControlePost

class ControleSistema:
    def __init__(self) -> None:
        self.__controleUsuario = ControleUsuario(self)
        self.__controlePost = ControlePost(self)

    @property
    def controleUsuario(self):
        return self.__controleUsuario

    @property
    def controlePost(self):
        return self.__controlePost


if __name__ == "__main__":
    controleUs = ControleSistema()
    controleUs.controleUsuario.tela_inicial()
    controleUs.controlePost.listar_posts()
