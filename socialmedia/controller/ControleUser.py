from socialmedia.usuario import Usuario
from socialmedia.admin import Admin


class ControleUsuario:
    def __init__(self, controladorSistema, tela_usuario):
        self.__listaUsuarios = []
        self.__listaAdmins = []
        self.__controleSistema = controladorSistema
        self.__tela_usuario = tela_usuario

    @property
    def lista_usuarios(self):
        return self.__listaUsuarios

    @property
    def lista_admins(self):
        return self.__listaAdmins

    @property
    def controleSistema(self):
        return self.__controle

    @lista_usuarios.setter
    def lista_usuarios(self, nova_lista):
        self.__listaUsuarios = nova_lista

    @lista_admins.setter
    def lista_admins(self, nova_lista):
        self.__listaAdmins = nova_lista

    def pegar_username_senha(self):
        dictLogin = self.__tela_usuario.propmptLogin()
        return dictLogin

    def adicionar_admin(self, username, senha):
        assert self.usuario_is_disponivel(username=username)
        self.lista_admins.append(Admin(username, senha))
        return True

    def cadastrar(self):
        dictLogin = self.pegar_username_senha()  # mexendo com a tela
        username = dictLogin["username"]
        senha = dictLogin["senha"]
        assert self.usuario_is_disponivel(username)
        self.lista_usuarios.append(Usuario(username, senha))
        return True  # eu quero mandar pros posts, como eu chamo o controle de posts??
        # passar na tela??

    def logar(self, controleSistema, username, senha):
        # pegar da tela email e senha(input)
        assert self.usuario_is_disponivel(username)
        for u in self.lista_usuarios + self.lista_admins:
            if u.username == username and u.senha == senha:
                controleSistema.usuario_logado = u
                return "Logado com sucesso"
        return "Usuário ou senha inválidos"  # retornar tela???

    def deslogar(self):
        self.controleSistema.usuario_logado = None
        return "Deslogado com sucesso"

    def usuario_is_disponivel(self, username):
        for u in self.lista_usuarios + self.lista_admins:
            if u.username == username:
                return False
        return True


# controlador sistema instancia os controles e passa self.
