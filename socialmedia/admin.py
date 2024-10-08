from usuario import Usuario


class Admin(Usuario):
    def __init__(self, username: str, senha: str):
        super().__init__(username=username, senha=senha)