# socialmedia/exceptions.py

class UsuarioJaExisteException(Exception):
    def __init__(self, message="Usuário já existe"):
        self.message = message
        super().__init__(self.message)

class UsuarioNaoEncontradoException(Exception):
    def __init__(self, message="Usuário não encontrado"):
        self.message = message
        super().__init__(self.message)

class CredenciaisInvalidasException(Exception):
    def __init__(self, message="Credenciais inválidas"):
        self.message = message
        super().__init__(self.message)

class PostNaoEncontradoException(Exception):
    def __init__(self, message="Post não encontrado"):
        self.message = message
        super().__init__(self.message)

class ComentarioNaoEncontradoException(Exception):
    def __init__(self, message="Comentário não encontrado"):
        self.message = message
        super().__init__(self.message)

class AcaoNaoAutorizadaException(Exception):
    def __init__(self, message="Ação não autorizada"):
        self.message = message
        super().__init__(self.message)

class EntradaInvalidaException(Exception):
    def __init__(self, message="Entrada inválida"):
        self.message = message
        super().__init__(self.message)

class UsuarioError(Exception):
    pass

class UsuarioJaExistenteError(UsuarioError):
    def __init__(self, username):
        self.message = f"Usuário '{username}' já existe."
        super().__init__(self.message)

class CredenciaisInvalidasError(UsuarioError):
    def __init__(self):
        self.message = "Usuário ou senha inválidos."
        super().__init__(self.message)

class CampoVazioError(UsuarioError):
    def __init__(self, campo):
        self.message = f"O campo '{campo}' não pode ser vazio."
        super().__init__(self.message)