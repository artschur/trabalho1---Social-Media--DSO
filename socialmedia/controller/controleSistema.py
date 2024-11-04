from socialmedia.controller.controleUsario import ControleUsuario
from socialmedia.controller.controlePost import ControlePost
from socialmedia.services.relatorio import Relatorio
from socialmedia.controller.controleTopicos import ControleTopico
from socialmedia.controller.controleComentario import ControleComentario


class ControleSistema:
    def __init__(self) -> None:
        self.__controleUsuario = ControleUsuario(self)
        self.__controleTopico = ControleTopico(self)
        self.__controlePost = ControlePost(self, self.controleTopico)
        self.__relatorio = Relatorio(self.__controlePost)
        self.__usuarioLogado = None
        self.__topico_atual = None

    @property
    def controleUsuario(self):
        return self.__controleUsuario

    @property
    def relatorio(self):
        return self.__relatorio

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

    def telainit(self):
        return self.controleUsuario.tela_inicial()

    def logout(self):
        self.usuarioLogado = None
        self.topico_atual = None

    def return_relatorios(self):
        print()
        return (self.relatorio.post_mais_curtido(), self.relatorio.topico_com_mais_posts(), self.relatorio.topico_com_mais_interacoes(), self.relatorio.autor_mais_curtido())



def inicializaSistema():
    sis = ControleSistema()

    while True:
        print("Bem vindo ao SocialBlogs!\nFaça login ou cadastre-se para continuar. Nos somos uma rede social baseada em tópicos.")
        user = sis.telainit()

        if user is None or "user" not in user:
            print("Login falhou. Tente novamente.")
            continue
        print(f"Bem-vindo, {user['user'].username}!")
        sis.usuarioLogado = user["user"]

        while sis.usuarioLogado:
            topico_selecionado = sis.controleTopico.get_topico()
            if topico_selecionado is None:
                continue

            sis.topico_atual = topico_selecionado
            result = sis.controlePost.listar_posts(sis.topico_atual)

            if result == "logout":
                sis.logout()
                break