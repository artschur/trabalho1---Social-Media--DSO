class TelaTopico:
    def obter_nome_topico(self):
        return input("Digite o nome do novo tópico: ").strip()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_lista_topicos(self, topicos):
        print("\n=== Lista de Tópicos ===")
        for i, topico in enumerate(topicos, 1):
            print(f"{i} - {topico.nome}")
        print("0 - Adicionar novo tópico")

        return input("Digite o número do tópico para ver os posts (ou 0 para voltar): ")



    def adicionar_topico(self):
        return input("Digite o nome do novo tópico: ")
