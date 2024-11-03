from socialmedia.topico import Topico
from socialmedia.views.telaTopico import TelaTopico

class ControleTopico:
    def __init__(self):
        self.__topicos = [Topico("Economia"), Topico("Tecnologia"), Topico("Esportes")]
        self.__telaTopico = TelaTopico()

    @property
    def topicos(self):
        return self.__topicos

    @property
    def telaTopico(self):
        return self.__telaTopico

    def get_topico(self) -> Topico:
        escolha = int(self.telaTopico.mostrar_lista_topicos(self.topicos))
        print(escolha)
        if escolha == 0:
            self.adicionar_topico()
        elif 1 <= escolha <= len(self.__topicos) - 1:
            return self.__topicos[escolha - 1]
        else:
            print("Escolha inválida.")
            return None # esportes esta retornando isso pq?

    def adicionar_topico(self):
        novo_topico_nome = self.telaTopico.adicionar_topico()
        if novo_topico_nome and all(t.nome != novo_topico_nome for t in self.__topicos):
            novo_topico = Topico(novo_topico_nome)
            self.__topicos.append(novo_topico)
            print(f"Tópico '{novo_topico_nome}' adicionado com sucesso!")
        else:
            print("Nome de tópico inválido ou já existente.")