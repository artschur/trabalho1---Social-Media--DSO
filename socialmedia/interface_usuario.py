from usuario import Usuario  # Certifique-se de importar a classe correta
from app import Aplicativo   # Importar a classe Aplicativo
from comment_manager import CommentManager  # Para gerenciar comentários
from admin import Admin  # Importar a classe Admin
from topico import Topico  # Importar a classe Topico
from post import Post  # Importar a classe Post

class InteracaoUsuario:
    def __init__(self, usuario, aplicativo):
        self.usuario = usuario
        self.aplicativo = aplicativo

    def mostrar_feed(self):
        print("======== Feed de Tópicos =========")
        for idx, topico in enumerate(self.aplicativo.topicos, start=1):  
            print(f"{idx}. {topico.name}")
        print("0. Sair")
        print("==================================")
    
    def escolher_topico(self):
        while True:
            self.mostrar_feed()
            escolha_topico = input("Escolha um tópico pelo número ou digite 0 para sair: ")

            if escolha_topico.isdigit():
                escolha_topico = int(escolha_topico)
                if escolha_topico == 0:
                    break
                elif 1 <= escolha_topico <= len(self.aplicativo.topicos):  # Correção feita aqui
                    topico_escolhido = self.aplicativo.topicos[escolha_topico - 1]
                    self.mostrar_posts(topico_escolhido)
                else:
                    print("Escolha inválida. Tente novamente.")
            else:
                print("Por favor, digite um número.")

    def mostrar_posts(self, topico):
        print(f"\n======== Posts em {topico.name} =========")
        if not topico.posts:
            print("Nenhum post encontrado neste tópico.")
            return

        for idx, post in enumerate(topico.posts, start=1):
            print(f"{idx}. {post.conteudo} (Autor: {post.autor.username})")
        print("0. Voltar ao feed")

        escolha_post = input("Escolha um post para interagir ou digite 0 para voltar: ")

        if escolha_post.isdigit():
            escolha_post = int(escolha_post)
            if escolha_post == 0:
                return
            elif 1 <= escolha_post <= len(topico.posts):  # Corrigido para aceitar posts corretamente
                post_escolhido = topico.posts[escolha_post - 1]  # Ajustado para índice correto
                self.interagir_com_post(post_escolhido)
            else:
                print("Escolha inválida.")
        else:
            print("Por favor, insira um número válido.")
        
    def interagir_com_post(self, post):
        while True:
            print(f"\n======== Interagindo com Post =========")
            print(f"Post: {post.conteudo} (Autor: {post.autor.username})")
            print(f"Likes: {post.count_likes()}, Comentários: {post.count_comentarios()}")
            print("\n1. Curtir Post")
            print("2. Comentar Post")
            print("3. Ver Comentários")
            print("0. Voltar para os posts")

            escolha = input("Escolha uma ação: ")

            if escolha == "1":
                self.usuario.curtir_post(post)
                print("Você curtiu o post!")
            elif escolha == "2":
                comentario_conteudo = input("Digite seu comentário: ") 
                comment_manager = CommentManager()
                self.usuario.comentar(comentario_conteudo, post, comment_manager)   
                print("Comentário adicionada com sucesso!")
            elif escolha == "3":
                self.mostrar_comentarios(post)
            elif escolha == "0":
                break
            else:
                print("Escolha inválida.")

    def mostrar_comentarios(self, post):
        print(f"\n======== Comentários =========")
        if not post.comentarios:
            print("Nenhum comentário neste post.")
        else:
            for idx, comentario in enumerate(post.comentarios, start=1):  # Ajustado para começar do índice 1
                print(f"{idx}. {comentario.conteudo} (Autor: {comentario.autor.username})")
                print(f"Likes: {comentario.count_likes()}")  # Interpolação correta
            print("0. Voltar")
        
        escolha_comentario = input("Escolha um comentário para curtir ou digite 0 para voltar: ")

        if escolha_comentario.isdigit():
            escolha_comentario = int(escolha_comentario)
            if escolha_comentario == 0:
                return
            elif 1 <= escolha_comentario <= len(post.comentarios):
                comentario_escolhido = post.comentarios[escolha_comentario - 1]
                self.usuario.curtir_comentario(comentario_escolhido)
                print(f"Você curtiu o comentário: '{comentario_escolhido.conteudo}'")
            else:
                print("Escolha inválida.")
        else:
            print("Por favor, insira um número válido.")
