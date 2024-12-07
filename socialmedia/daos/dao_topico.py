from socialmedia.daos.dao_abstract import DAO
from socialmedia.topico import Topico

class TopicosDAO(DAO):
    def __init__(self):
        super().__init__('topico.pkl')

    def adicionarTopico(self, topico):
        if((topico is not None) and isinstance(topico, Topico) and isinstance(topico.id, str)):
            super().add(topico.id, topico)

    def updateTopico(self, topico: Topico):
        if((topico is not None) and isinstance(topico, Topico) and isinstance(topico.id, str)):
            super().update(topico.id, topico)

    def getTopico(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def removeTopico(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)

    def get_all(self):
        return list(super().get_all())
