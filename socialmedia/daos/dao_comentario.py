from socialmedia.comentario import Comentario
from socialmedia.daos.dao_abstract import DAO

class ComentariosDAO(DAO):
    def __init__(self):
        super().__init__('comentarios.pkl')

    def adicionarComentario(self, comentario: Comentario):
        if (comentario is not None and
                isinstance(comentario, Comentario) and
                isinstance(comentario.id, str)):
            super().add(comentario.id, comentario)

    def updateComentario(self, comentario: Comentario):
        if (comentario is not None and
            isinstance(comentario, Comentario) and
            isinstance(comentario.id, str)):
            super().update(comentario.id, comentario)

    def getCometario(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def removeComentario(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        return list(self._DAO__objects.values())