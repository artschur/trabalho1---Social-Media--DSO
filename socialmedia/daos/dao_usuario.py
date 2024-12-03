from socialmedia.daos.dao_abstract import DAO
from socialmedia.usuario import Usuario

class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuario.pkl')

    def addUsuario(self, usuario: Usuario):
        if((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.username, str)):
            super().add(usuario.username, usuario)

    def updateUsuario(self, usuario: Usuario):
        if((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.username, str)):
            super().update(usuario.username, usuario)

    def getUsuario(self, key: str):
        try:
            if isinstance(key, str):
                return super().get(key)
        except:
            raise KeyError

    def get_all_usuarios(self): #mais rapido para auth.
        return super().cache
    def removeUsuario(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)