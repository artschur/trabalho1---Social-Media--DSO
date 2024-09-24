from topico import Topico


class Aplicativo:
    def __init__(self) -> None:
        self.__usuarios = []
        self.__admins = []
        self.__topicos = []  # Uma seção pode ter muitos posts
        self.__topicos.append(Topico("Tecnologia"))
        self.__topicos.append(Topico("Economia"))
        self.__topicos.append(Topico("Cultura"))  # topicos predefinidos.

    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def admins(self):
        return self.__admins

    @property
    def topicos(self):
        return self.__topicos

    def add_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def add_admin(self, admin):
        self.__admins.append(admin)
