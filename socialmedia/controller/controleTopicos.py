from socialmedia.topico import Topico
from socialmedia.views.telaTopico import TelaTopico


class ControleTopico:
    __instance = None
    __topicos = None  # Class variable to store topics

    def __init__(self, controleSistema):
        if ControleTopico.__topicos is None:
            # Only initialize the topics list once
            ControleTopico.__topicos = [Topico("Economia"), Topico("Tecnologia"),
                                        Topico("Esportes")]
        self.__telaTopico = TelaTopico()
        self.__controleSistema = controleSistema

    @property
    def topicos(self):
        return ControleTopico.__topicos  # Use class variable instead of instance variable

    @property
    def controleSistema(self):
        return self.__controleSistema

    @property
    def telaTopico(self):
        return self.__telaTopico

    def get_topico(self) -> Topico:
        while True:
            try:
                escolha = self.telaTopico.mostrar_lista_topicos(self.topicos)
                if escolha.lower() == 'e':
                    self.controleSistema.logout()
                    return None
                escolha = int(escolha)

                if escolha == 0:
                    self.adicionar_topico()
                    continue
                elif 1 <= escolha <= len(self.topicos):
                    topico_selecionado = self.topicos[escolha - 1]
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
        if any(t.nome.lower() == novo_topico_nome.lower() for t in self.topicos):
            print("Tópico já existe.")
            return None
        novo_topico = Topico(novo_topico_nome)
        self.topicos.append(novo_topico)
        print(f"Tópico '{novo_topico_nome}' adicionado com sucesso!")
        return novo_topico
