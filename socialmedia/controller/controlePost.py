from socialmedia.post import Post
from socialmedia.topico import Topico
from socialmedia.views.telaPost import TelaPost
from socialmedia.comentario import Comentario
from socialmedia.admin import Admin
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
            return self.listar_posts()

        try:
            dados_post = self.__telaPost.tela_criar_post()
            if dados_post['titulo'] and dados_post['conteudo'] and dados_post['topico']:
                novo_post = Post(dados_post['titulo'], dados_post['conteudo'], usuarioLogado, Topico(dados_post['topico']))
                self.posts.append(novo_post)
                return self.post_individual(self.posts[-1])
            else:
                raise PostCreationError("Erro: Título ou conteúdo do post está faltando.")
        except PostCreationError as e:
            return False

    # def obter_topico_por_nome(self, nome_topico: str):
    #     for t in self.__controleSistema.topicos:
    #         if t.nome == nome_topico:
    #             return t
    #     return Topico(nome_topico)

    def listar_posts(self):
        while True:
            escolha = int(self.telaPost.mostrar_lista_posts(self.posts))
            if escolha == 1:
                self.criar_post()
            try:
                indice = int(escolha) - 2
                if 0 <= indice < len(self.posts):
                    print(self.posts[indice])
                    self.post_individual(self.posts[indice])
                else:
                    raise IndexError("Escolha Inválida")
            except ValueError:
                raise ValueError("Escolha Inválida")
            except IndexError as e:
                raise IndexError(str(e))

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
