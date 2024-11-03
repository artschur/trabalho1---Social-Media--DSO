from socialmedia.post import Post
from socialmedia.topico import Topico
from socialmedia.views.telaPost import TelaPost
from socialmedia.comentario import Comentario
from socialmedia.admin import Admin
from socialmedia.controller.controleTopicos import ControleTopico
# from
class NotLoggedInError(Exception):
    pass

class PostCreationError(Exception):
    pass

class ControlePost:
    def __init__(self, controladorSistema):
        self.__posts = []
        self.__controleSistema = controladorSistema
        self.__telaPost = TelaPost()
        self.__controleTopicos = ControleTopico()


    @property
    def controleSistema(self):
        return self.__controleSistema

    @property
    def controleTopicos(self):
        return self.__controleTopicos

    @property
    def telaPost(self):
        return self.__telaPost

    @property
    def posts(self):
        return self.__posts

    def criar_post(self):
        usuarioLogado = self.__controleSistema.usuarioLogado
        if not isinstance(usuarioLogado, Admin):
            print("Você precisa estar logado como admin para criar um post.")
            return False

        dados_post = self.__telaPost.tela_criar_post(self.controleTopicos.topicos)
        if not (dados_post['titulo'] and dados_post['conteudo']):
            print("Erro: Título ou conteúdo do post está faltando.")
            return False

        topico_escolhido = dados_post['topico']
        if not topico_escolhido:
            print("Tópico inválido.")
            return False

        novo_post = Post(dados_post['titulo'], dados_post['conteudo'], usuarioLogado, topico_escolhido)
        self.__posts.append(novo_post)
        self.post_individual(novo_post)
        return True

    def listar_posts(self, topico=None):
        topico_posts = self.posts
        if topico:
            topico_posts = [post for post in self.posts if post.topico.nome == topico.nome]
            if topico_posts == []:
                print("Nenhum post encontrado para este tópico.")
                print("Mostrando todos")
                topico_posts = self.posts

        escolha = int(self.telaPost.mostrar_lista_posts(topico_posts))
        if escolha == 1:
            self.criar_post()
        else:
            indice = escolha - 2
            if 0 <= indice < len(topico_posts):
                self.post_individual(topico_posts[indice])
            elif escolha == -1:
                print(self.controleTopicos.get_topico())

    def curtir_comentario(self, comentario):
        if self.__controleSistema.usuario_logado not in comentario.likes:
            comentario.likes.append(self.__controleSistema.usuario_logado)
            print("Comentário curtido com sucesso!")
        else:
            print("Você já curtiu este comentário.")
        self.listar_posts()

    def comentar(self, post):
        conteudo = self.telaPost.comentar_post()
        comentario = Comentario(conteudo, self.__controleSistema.usuario_logado)
        post.comentarios.append(comentario)
        self.listar_posts()

    def interage_comentarios(self, post):
        escolha = self.telaPost.mostrar_comentarios(post)
        if escolha == "1":
            try:
                indice_comentario = int(self.telaPost.selecionar_comentario(post)) - 1
                if 0 <= indice_comentario < len(post.comentarios):
                    self.curtir_comentario(post.comentarios[indice_comentario])
                    self.listar_posts()
            except ValueError:
                print("Digite um número válido.")
        elif escolha == "2":
            self.listar_posts()
        else:
            raise ValueError("Escolha inválida")

    def post_individual(self, post):
        escolha = int(self.telaPost.vizualizar_post(post))
        acoes_com_post = {1: self.curtir_post, 2: self.comentar, 3: self.interage_comentarios}
        acoes_sem_post = {4: self.listar_posts}

        if escolha in acoes_com_post:
            acoes_com_post[escolha](post)
        elif escolha in acoes_sem_post:
            acoes_sem_post[escolha]()
        else:
            print("Escolha inválida")
            self.post_individual(post)

    def curtir_post(self, post):
        if self.__controleSistema.usuarioLogado not in post.likes:
            post.likes.append(self.__controleSistema.usuarioLogado)
        else:
            raise ValueError("Você já curtiu esse post")
        return self.listar_posts()
