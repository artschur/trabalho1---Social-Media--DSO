class TelaPost:
    def tela_criar_post(self, lista_topicos):
        print("\n=== Criar Novo Post ===")
        titulo = input("Digite o título do post: ").strip()
        conteudo = input("Digite o conteúdo do post: ").strip()

        print("\nSelecione o Tópico:")
        for i, topico in enumerate(lista_topicos, 1):
            print(f"{i} - {topico.nome}")

        topico_escolhido = int(input("Escolha o número do tópico: "))
        topico = lista_topicos[topico_escolhido - 1]
        return {"titulo": titulo, "conteudo": conteudo, "topico": topico}
    
    def mostrar_lista_posts(self, posts, topico=None):
        print("\n=== Lista de Posts ===")
        if topico:
            print(f"=== Tópico: {topico.nome} ===")
        if not posts:
            print("Nenhum post encontrado")
            return
        print("1 - Criar Post")
        for i, post in enumerate(posts, 2):
            print(f"{i} - {post.titulo}")

        return input("Digite o numero do post para ver mais detalhes(0 para voltar e 'E' para logout.): ")

    def mostrar_comentarios(self, post):
        print("\n=== Comentários ===")
        for i, comentario in enumerate(post.comentarios, 1):
            print(f"{i}. '{comentario.conteudo}' - {comentario.autor.username} | {comentario.count_likes} likes")
        print("\n1. Curtir Comentário")
        print("2. Voltar")
        return input("Escolha uma opção: ")

    def selecionar_comentario(self, post):
        print("\nSelecione o número do comentário que deseja curtir:")
        for i, comentario in enumerate(post.comentarios, 1):
            print(
                f"{i}. '{comentario.conteudo}' - {comentario.autor.username} | {comentario.count_likes} likes")
        return input("Digite o número do comentário: ")

    def comentar_post(self):
        return input("Digite o seu comentário: ")


    def vizualizar_post(self, post):
        print(f"\n=== {post.titulo} ===")
        print(f"Autor: {post.autor.username}")
        print(f"Tópico: {post.topico.nome}")
        print(f"\n{post.conteudo}")
        print(f"\nLikes: {post.count_likes()}")
        print(f"Comentários: {post.count_comentarios()}")
        print("\n1. Curtir post")
        print("2. Comentar")
        print("3. Ver comentários")
        print("4. Voltar")
        return input("Escolha uma opção: ")