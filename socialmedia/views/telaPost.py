class TelaPost:
    def tela_criar_post(self, lista_topicos):
        print("\nCriar Novo Post ")
        titulo = input("Digite o título do post: ").strip()
        conteudo = input("Digite o conteúdo do post: ").strip()

        print("\nSelecione o Tópico:")
        for i, topico in enumerate(lista_topicos, 1):
            print(f"{i} - {topico.nome}")

        topico_escolhido = int(input("Escolha o número do tópico: "))
        topico = lista_topicos[topico_escolhido - 1]
        return {"titulo": titulo, "conteudo": conteudo, "topico": topico}
    
    def mostrar_lista_posts(self, posts, topico=None):
        if topico:
            print(f"\nLista de Posts - {topico.nome}")
        if not posts:
            print("Lista de Posts - Nenhum post encontrado")
            return
        print("1. Criar Post")
        for i, post in enumerate(posts, 2):
            print(f"{i}. {post.titulo}")

        return input("Digite o numero do post para ver mais detalhes(0 para voltar e 'E' para logout.): ")

    def mostrar_comentarios(self, post):
        print("\nComentários")
        for i, comentario in enumerate(post.comentarios, 1):
            print(f"{i}. '{comentario.conteudo}' - {comentario.autor.username} | {comentario.count_likes} likes")
        print("\n1. Interagir com Comentário")
        print("2. Voltar")
        escolha = input("Escolha uma opção: ")
        if escolha == "2":
            return "voltar"
        return escolha

    def selecionar_comentario(self, post):
        print("\nSelecione o número do comentário que deseja interagir:")
        for i, comentario in enumerate(post.comentarios, 1):
            print(
                f"{i}. '{comentario.conteudo}' - {comentario.autor.username} | {comentario.count_likes} likes")
        return input("Digite o número do comentário: ")

    def comentar_post(self):
        return input("Digite o seu comentário: ")


    def vizualizar_post(self, post):
        print(f"\n{post.titulo} - {post.autor.username}")
        print(f"Tópico: {post.topico.nome}")
        print(f"\n{post.conteudo}")
        print(f"\n{post.count_likes()} likes.")
        print(f"Comentários: {post.count_comentarios()}")
        print("\n1. Curtir post")
        print("2. Comentar")
        print("3. Ver comentários")
        print("4. Voltar")
        return input("Escolha uma opção: ")