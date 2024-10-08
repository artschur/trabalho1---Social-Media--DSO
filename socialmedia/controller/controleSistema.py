from socialmedia.controller.controleUsario import ControleUsuario


class ControleSistema:
    def __init__(self) -> None:
        self.__controleUsuario = ControleUsuario(self)

    @property
    def controleUsuario(self):
        return self.__controleUsuario


if __name__ == "__main__":
    controleUs = ControleSistema()
    controleUs.controleUsuario.tela_login()
