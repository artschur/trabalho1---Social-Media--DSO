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
        return self.__controleSistema

    @lista_usuarios.setter
    def lista_usuarios(self, nova_lista):
        self.__lista_usuarios = nova_lista

    @lista_admins.setter
    def lista_admins(self, nova_lista):
        self.__lista_admins = nova_lista

# talvez podemos retirar os metodos de pegar da tela, e chamar direto do cadastro e login, mas não sei 

    def pegar_username_senha_login(self): # puxar as infos da tela, só que do login 
        dictLogin = self.__tela_usuario.tela_login()
        return dictLogin
    
    def pegar_username_senha_cadastro(self): # puxar as infos da tela, só que do cadastro, não do login 
        dictCadastro = self.__tela_usuario.tela_cadastro()
        return dictCadastro
    
    def adicionar_admin(self, username, senha):
        assert self.usuario_is_disponivel(username=username)
        self.lista_admins.append(Admin(username, senha))
        return True

    def cadastrar(self):
        dictLogin = self.pegar_username_senha_cadastro()  # chama a tela, e puxa as infos do cadastro 
        username = dictLogin["username"]
        senha = dictLogin["senha"]
        if not self.usuario_is_disponivel(username): # dei uma pesquisada, e vi que o assert é mais para testes, e o raise é para erros 
            # "print("Erro: Usuário já cadastrado" ou raise Exception("Usuário já cadastrado")" não sabia qual usar
            return False
        self.lista_usuarios.append(Usuario(username, senha))
        return True

    def logar(self):
        dictLogin = self.pegar_username_senha_login()
        if not dictLogin["username"]:
            return False 
        
        if not dictLogin["senha"]:
            return False
        
        username = dictLogin["username"]
        senha = dictLogin["senha"]

        resultado_login = self.validar_login(username, senha) 
        return resultado_login 

    def validar_login(self, username, senha): 
        if self.usuario_is_disponivel(username):
            return False # talvez printar uma mensagem de erro, ou lançar uma exceção 
        
        for u in self.__lista_usuarios + self.__lista_admins:
            if u.username == username and u.senha == senha:
                self.__controleSistema.usuario_logado = u
                return True
        return False # dnv talvez printar mensagem  
    
    def deslogar(self):
        self.controleSistema.usuario_logado = None
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
        assert escolha in escolhas.keys() # pensei em alterar isso, mas não tenho certeza se vai funcionar
        return escolhas[escolha]()

    def tela_login(self):
        dictLogin = self.__tela_usuario.tela_login()

        if not dictLogin["username"]:
            return "O nome de usuário não pode ser vazio."

        if not dictLogin["senha"]:
            return "A senha não pode ser vazia."

        login_result = self.logar(dictLogin["username"], dictLogin["senha"])

        if login_result is True:
            print("Logado com sucesso!")
            return True
        else:
            print("erro no login")
            return False
