from socialmedia.usuario import Usuario
from socialmedia.admin import Admin
from socialmedia.views.telaUsuario import TelaUsuario


class ControleUsuario:
    def __init__(self, controladorSistema):
        self.__lista_usuarios = [Admin("a", "a")]
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
        return self.__controleSistema
    
    def adicionar_admin(self, username, senha):
        assert self.usuario_is_disponivel(username=username)
        self.lista_admins.append(Admin(username, senha))
        return True

    def cadastrar(self, usuario : Usuario):
        assert self.usuario_is_disponivel(usuario.username), "Usuário já existe"
        self.lista_usuarios.append(usuario)
        return usuario
    def login_auth(self, username, senha):
        assert not self.usuario_is_disponivel(username), "Usuário não encontrado"

        for u in self.__lista_usuarios + self.__lista_admins:
            if u.username == username and u.senha == senha:
                self.__controleSistema.usuarioLogado = u 
                return {"user": u, "admin": isinstance(u, Admin)}

        return "Usuário ou senha inválidos"

    def deslogar(self):
        self.controleSistema.usuarioLogado = None
        return "Deslogado com sucesso"


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

        if login_result != False: ##
            print("Logado com sucesso!")
            return login_result
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
            usuario = self.cadastrar(Usuario(dictCadastro["username"], dictCadastro["senha"]))
            print("Cadastro realizado com sucesso!")
            return {"user": usuario, "admin": isinstance(usuario, Admin)}
        except AssertionError as e:
            print(f"Erro no cadastro: {e}")

    def tela_logout(self):
        self.deslogar()
        print("Você foi deslogado com sucesso!")
        return True
