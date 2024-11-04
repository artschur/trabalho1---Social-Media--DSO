class TelaComentario:
    def tela_editar_comentario(self):
        print("\n=== Editar Comentário ===")
        novo_conteudo = input("Digite o novo conteúdo do comentário: ").strip()
        return novo_conteudo

    def mostrar_opcoes_comentario(self):
        print("\n=== Opções do Comentário ===")
        print("1. Curtir comentário")
        print("2. Editar comentário")
        print("3. Deletar comentário")
        print("4. Voltar")
        return input("Escolha uma opção: ")

    def confirmar_delecao(self):
        print("\nTem certeza que deseja deletar este comentário?")
        print("1. Sim")
        print("2. Não")
        return input("Escolha uma opção: ") == "1"

    def mostrar_mensagem(self, mensagem):
        print(mensagem)