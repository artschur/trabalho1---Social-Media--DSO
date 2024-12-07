from uuid import uuid4

class Usuario:
    def __init__(self, username: str, senha: str) -> None:
        self.__username = username
        self.__senha = senha

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, newname):
        self.__username = newname

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, newsenha):
        self.__senha = newsenha
