class TelaPost:
    def tela_criar_post(self, lista_topicos):
        print("\n=== Criar Novo Post ===")
        titulo = input("Digite o título do post: ").strip()
        conteudo = input("Digite o conteúdo do post: ").strip()
        
        print("\nSelecione o Tópico:")
        for i, topico in enumerate(lista_topicos, 1):
            print(f"{i} - {topico}")
        
        topico_escolhido = int(input("Escolha o número do tópico: "))
        topico = lista_topicos[topico_escolhido - 1]
        
        return {"titulo": titulo, "conteudo": conteudo, "topico": topico}
    
    def mostrar_lista_posts(self, posts):
        print("\n=== Lista de Posts ===")
        if not posts:
            print("Nenhum post encontrado")
            return #talvez 0
        
        for i, post in enumerate(posts, 1):
            print(f"{i} - {post.titulo}")

        return int(input("Digite o numero do post para ver mais detalhes (ou 0 pra voltar): "))
    
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