from socialmedia.usuario import Usuario
from socialmedia.admin import Admin
from socialmedia.views.telaUsuario import TelaUsuario
from socialmedia.exceptions.exceptions import *


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
        if not self.usuario_is_disponivel(username):
            raise UsuarioJaExistenteError(username)
        admin = Admin(username, senha)
        self.lista_admins.append(admin)
        return admin

    def cadastrar(self, usuario: Usuario):
        if not self.usuario_is_disponivel(usuario.username):
            raise UsuarioJaExistenteError(usuario.username)
        self.lista_usuarios.append(usuario)
        return usuario

    def login_auth(self, username, senha):
        for u in self.__lista_usuarios + self.__lista_admins:
            if u.username == username and u.senha == senha:
                self.controleSistema.usuarioLogado = u
                return {"user": u, "admin": isinstance(u, Admin)}
        raise CredenciaisInvalidasError()
        return None

    def usuario_is_disponivel(self, username):
        for u in self.lista_usuarios + self.lista_admins:
            if u.username == username:
                return False
        return True

    def tela_login(self):
        try:
            dictLogin = self.__tela_usuario.tela_login()

            if not dictLogin["username"] or not dictLogin["senha"]:
                print("Username e senha são obrigatórios.")
                return None

            login_result = self.login_auth(dictLogin["username"], dictLogin["senha"])
            if login_result:
                return login_result
            return None
        except CredenciaisInvalidasError as e:
            print(e.message)
            self.controleSistema.logout()
            return None
        except Exception as e:
            print(f"Erro no login: {str(e)}")
            return None

    def tela_inicial(self):
        try:
            escolha = self.__tela_usuario.tela_inicial()
            escolhas = {
                "1": self.tela_login,
                "2": self.tela_cadastro,
                "3": self.tela_logout,
            }
            if escolha not in escolhas:
                print("Opção inválida!")
                return None

            result = escolhas[escolha]()
            return result
        except Exception as e:
            print(f"Erro: {str(e)}")
            return None
    def tela_cadastro(self):
        dictCadastro = self.__tela_usuario.tela_cadastro()

        if not dictCadastro["username"]:
            raise CampoVazioError("username")

        if not dictCadastro["senha"]:
            raise CampoVazioError("senha")

        if not dictCadastro["admin"]:
            raise CampoVazioError("admin")

        try:
            if dictCadastro["admin"] == "s":
                usuario = self.adicionar_admin(dictCadastro["username"], dictCadastro["senha"])
            else:
                usuario = self.cadastrar(Usuario(dictCadastro["username"], dictCadastro["senha"]))
            self.controleSistema.usuarioLogado = usuario
            print("Cadastro realizado com sucesso!")
            return {"user": usuario, "admin": isinstance(usuario, Admin)}
        except UsuarioJaExistenteError as e:
            print(e.message)

    def tela_logout(self):
        self.controleSistema.logout()
        print("Até mais!")
        return exit()
