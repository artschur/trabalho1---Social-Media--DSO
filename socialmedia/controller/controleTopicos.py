from socialmedia.topico import Topico
from socialmedia.views.telaTopico import TelaTopico
from socialmedia.daos.dao_topico import TopicosDAO

class ControleTopico:
    def __init__(self, controleSistema):
        self.__telaTopico = TelaTopico()
        self.__controleSistema = controleSistema
        self.__dao = TopicosDAO()
    @property
    def dao(self):
        return self.__dao
    @property
    def controleSistema(self):
        return self.__controleSistema

    @property
    def telaTopico(self):
        return self.__telaTopico

    def get_topico(self) -> Topico:
        while True:
            try:
                escolha = self.telaTopico.mostrar_lista_topicos(self.dao.get_all())
                if escolha.lower() == 'e':
                    self.controleSistema.logout()
                    return None
                escolha = int(escolha)

                if escolha == 0:
                    self.adicionar_topico()
                    continue
                elif 1 <= escolha <= len(self.dao.get_all()):
                    print(self.dao.get_all())
                    topico_selecionado = self.dao.get_all()[escolha - 1]
                    return topico_selecionado
                else:
                    print("Escolha inválida.")
                    continue
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
    def adicionar_topico(self):
        novo_topico_nome = self.telaTopico.adicionar_topico()
        if not novo_topico_nome:
            print("Nome do tópico não pode estar vazio.")
            return None
        if any(t.nome.lower() == novo_topico_nome.lower() for t in self.dao.get_all()):
            print("Tópico já existe.")
            return None
        novo_topico = Topico(novo_topico_nome)
        self.dao.adicionarTopico(novo_topico)
        print(f"Tópico '{novo_topico_nome}' adicionado com sucesso!")
        return novo_topico
