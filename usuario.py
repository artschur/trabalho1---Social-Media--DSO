from comentario import Comentario

class Usuario:
    def __init__(self, username: str, email: str, senha: str) -> None:
        self.__username = username
        self.__email = email
        self.__senha = senha
        self.__logged_in = False

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, newname):
        self.__username = newname

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, newemail):
        self.__email = newemail
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, newsenha):
        self.__senha = newsenha

    @property
    def logged_in(self):
        return self.__logged_in
    
    def login(self):
        self.__logged_in = True

    def logout(self):
        self.__logged_in = False

    def comentar(self, comentario: str):
        