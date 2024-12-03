from socialmedia.usuario import Usuario
from socialmedia.admin import Admin
from socialmedia.views.telaUsuario import TelaUsuario
from socialmedia.exceptions.exceptions import *
from socialmedia.daos.dao_usuario import UsuarioDAO

class ControleUsuario:
    def __init__(self, controladorSistema):
        self.__controleSistema = controladorSistema
        self.__tela_usuario = TelaUsuario()
        self.__dao = UsuarioDAO()

    @property
    def dao(self):
        return self.__dao

    @property
    def controleSistema(self):
        return self.__controleSistema

    def adicionar_admin(self, username, senha):
        if not self.usuario_is_disponivel(username):
            raise UsuarioJaExistenteError(username)
        admin = Admin(username, senha)
        self.dao.addUsuario(admin)
        return admin

    def cadastrar(self, usuario: Usuario):
        if not self.usuario_is_disponivel(usuario.username):
            raise UsuarioJaExistenteError(usuario.username)
        self.dao.addUsuario(usuario)
        print(self.dao.get_all())
        return usuario

    def login_auth(self, username, senha):
        lista_users = self.dao.get_all_usuarios()
        print(lista_users)
        if lista_users[username] and lista_users[username].senha == senha:
            self.controleSistema.usuarioLogado = lista_users[username] # obj usuario
            return {"user": lista_users[username], "admin": isinstance(lista_users[username], Admin)}
        raise CredenciaisInvalidasError()

    def usuario_is_disponivel(self, username):
        if self.dao.getUsuario(username) == KeyError:
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
                "R": self.controleSistema.return_relatorios,
                "r": self.controleSistema.return_relatorios
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
                usuario = self.dao.addUsuario(Admin(dictCadastro["username"], dictCadastro["senha"]))
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
