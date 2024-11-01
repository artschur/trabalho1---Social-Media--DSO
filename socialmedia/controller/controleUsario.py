from socialmedia.usuario import Usuario
from socialmedia.admin import Admin
from socialmedia.views.telaUsuario import TelaUsuario


class ControleUsuario:
    def __init__(self, controladorSistema):
        self.__lista_usuarios = [Usuario("admin", "admin")]
        self.__lista_admins = []
        self.__controleSistema = controladorSistema
        self.__tela_usuario = TelaUsuario()

    @property
    def lista_usuarios(self):
        return self.__lista_usuarios

    @property
    def lista_admins(self):
        return self.__lista_admins

    @property
    def controleSistema(self):
        return self.__controle
    
    def adicionar_admin(self, username, senha):
        assert self.usuario_is_disponivel(username=username)
        self.lista_admins.append(Admin(username, senha))
        return True

    def cadastrar(self, username, senha):
        assert self.usuario_is_disponivel(username), "Usuário já existe"
        self.lista_usuarios.append(Usuario(username, senha))
        return True
    def login_auth(self, username, senha):
        assert not self.usuario_is_disponivel(username), "Usuário não encontrado"

        for u in self.__lista_usuarios + self.__lista_admins:
            if u.username == username and u.senha == senha:
                self.__controleSistema.usuario_logado = u
                return True

        return "Usuário ou senha inválidos"

    def deslogar(self):
        self.controleSistema.usuario_logado = None
        return "Deslogado com sucesso", exit()


    def usuario_is_disponivel(self, username):
        for u in self.lista_usuarios + self.lista_admins:
            if u.username == username:
                return False
        return True

    def tela_inicial(self):
        escolha = self.__tela_usuario.tela_inicial()
        escolhas = {
            "1": self.tela_login,
            "2": self.tela_cadastro,
            "3": self.tela_logout,
        }
        assert escolha in escolhas.keys()
        return escolhas[escolha]()

    def tela_login(self):
        dictLogin = self.__tela_usuario.tela_login()

        if not dictLogin["username"]:
            return "O nome de usuário não pode ser vazio."

        if not dictLogin["senha"]:
            return "A senha não pode ser vazia."

        login_result = self.login_auth(dictLogin["username"], dictLogin["senha"])

        if login_result is True:
            print("Logado com sucesso!")
            return True
        else:
            print("erro no login")
            return False

    def tela_cadastro(self):
        dictCadastro = self.__tela_usuario.tela_cadastro()
        if not dictCadastro["username"]:
            return "O nome de usuário não pode ser vazio."

        if not dictCadastro["senha"]:
            return "A senha não pode ser vazia."

        try:
            self.cadastrar(dictCadastro["username"], dictCadastro["senha"])
            print("Cadastro realizado com sucesso!")
            # Redirect to post control after successful registration
            self.__controleSistema.controlePost.listar_posts()
        except AssertionError as e:
            print(f"Erro no cadastro: {e}")

    def tela_logout(self):
        self.deslogar()
        print("Você foi deslogado com sucesso!")
        return True
