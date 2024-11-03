from socialmedia.exceptions.exceptions import (
    UsuarioNaoEncontradoException,
    CredenciaisInvalidasException,
    PostNaoEncontradoException,
    ComentarioNaoEncontradoException,
    AcaoNaoAutorizadaException,
    EntradaInvalidaException
)
from socialmedia.post import Post
from socialmedia.topico import Topico
from socialmedia.views.telaPost import TelaPost
from socialmedia.comentario import Comentario
from socialmedia.admin import Admin
from socialmedia.controller.controleTopicos import ControleTopico


class ControlePost:
    def __init__(self, controladorSistema, controleTopicos):
        self.__posts = []
        self.__controleSistema = controladorSistema
        self.__telaPost = TelaPost()
        self.__controleTopicos = controleTopicos
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

    def usuario_e_admin(self):
        usuarioLogado = self.__controleSistema.usuarioLogado
        if not isinstance(usuarioLogado, Admin):
            raise AcaoNaoAutorizadaException(
                "Você precisa estar logado como admin para criar um post.")

    def criar_post(self):
        try:
            self.usuario_e_admin()

            dados_post = self.__telaPost.tela_criar_post(self.controleTopicos.topicos)
            if not (dados_post['titulo'] and dados_post['conteudo']):
                raise EntradaInvalidaException("Erro: Título ou conteúdo do post está faltando.")

            topico_escolhido = dados_post['topico']
            if not topico_escolhido:
                raise EntradaInvalidaException("Tópico inválido.")

            novo_post = Post(dados_post['titulo'], dados_post['conteudo'],
                             self.__controleSistema.usuarioLogado, topico_escolhido)
            self.__posts.append(novo_post)
            self.post_individual(novo_post)
            return True
        except (AcaoNaoAutorizadaException, EntradaInvalidaException) as e:
            print(f"Erro: {e}")
            self.listar_posts()

    def listar_posts(self, topico=None):
        try:
            # Filter posts by topic if specified
            topico_posts = self.posts
            if topico:
                topico_posts = [post for post in self.posts if post.topico.nome == topico.nome]
                print(f"\n=== Posts do tópico: {topico.nome} ===")
                if not topico_posts:
                    print("Nenhum post encontrado para este tópico.")
                    print("Exibindo todos os posts.")
                    self.controleSistema.topico_atual = None
                    topico_posts = self.posts

            escolha = int(self.telaPost.mostrar_lista_posts(
                topico_posts,
                self.controleSistema.topico_atual
            ))

            if escolha == 1:  # Create new post
                self.criar_post()
                self.listar_posts(topico)
            elif escolha == 0:
                novo_topico = self.controleTopicos.get_topico()
                if novo_topico:
                    self.listar_posts(novo_topico)
            else:
                indice = escolha - 2
                if 0 <= indice < len(topico_posts):
                    self.post_individual(topico_posts[indice])
                else:
                    raise PostNaoEncontradoException("Post não encontrado.")

        except ValueError:
            print("Por favor, digite um número válido.")
            self.listar_posts(topico)
        except PostNaoEncontradoException as e:
            print(f"Erro: {e}")
            self.listar_posts(topico)
        except EntradaInvalidaException as e:
            print(f"Erro: {e}")
            self.listar_posts(topico)

    def curtir_comentario(self, comentario):
        try:
            usuario_logado = self.__controleSistema.usuarioLogado
            if usuario_logado not in comentario.likes:
                comentario.likes.append(usuario_logado)
                print("Comentário curtido com sucesso!")
            else:
                raise AcaoNaoAutorizadaException("Você já curtiu este comentário.")
            self.listar_posts(self.controleSistema.topico_atual)
        except AcaoNaoAutorizadaException as e:
            print(f"Erro: {e}")
            self.listar_posts(self.controleSistema.topico_atual)

    def comentar(self, post):
        try:
            conteudo = self.telaPost.comentar_post()
            if not conteudo:
                raise EntradaInvalidaException("Conteúdo do comentário não pode estar vazio.")
            comentario = Comentario(conteudo, self.__controleSistema.usuarioLogado)
            post.comentarios.append(comentario)
            self.listar_posts(self.controleSistema.topico_atual)
        except EntradaInvalidaException as e:
            print(f"Erro: {e}")
            self.listar_posts(self.controleSistema.topico_atual)

    def interage_comentarios(self, post):
        escolha = self.telaPost.mostrar_comentarios(post)
        if escolha == "1":
            try:
                indice_comentario = int(self.telaPost.selecionar_comentario(post)) - 1
                if 0 <= indice_comentario < len(post.comentarios):
                    self.curtir_comentario(post.comentarios[indice_comentario])
                else:
                    raise ComentarioNaoEncontradoException("Comentário não encontrado.")
            except (ValueError, ComentarioNaoEncontradoException, EntradaInvalidaException) as e:
                print(f"Erro: {e}")
        elif escolha == "2":
            self.listar_posts(self.controleSistema.topico_atual)
        else:
            print("Escolha inválida")
            self.listar_posts(self.controleSistema.topico_atual)

    def post_individual(self, post):
        try:
            escolha = int(self.telaPost.vizualizar_post(post))
            acoes_com_post = {1: self.curtir_post, 2: self.comentar, 3: self.interage_comentarios}
            acoes_sem_post = {4: self.listar_posts}

            if escolha in acoes_com_post:
                acoes_com_post[escolha](post)
            elif escolha in acoes_sem_post:
                acoes_sem_post[escolha](self.controleSistema.topico_atual)
            else:
                raise EntradaInvalidaException("Escolha inválida")
        except (ValueError, EntradaInvalidaException) as e:
            print(f"Erro: {e}")
            self.listar_posts(self.controleSistema.topico_atual)

    def curtir_post(self, post):
        try:
            if self.__controleSistema.usuarioLogado not in post.likes:
                post.likes.append(self.__controleSistema.usuarioLogado)
                print("Post curtido com sucesso!")
            else:
                raise AcaoNaoAutorizadaException("Você já curtiu esse post")
            return self.listar_posts(post.topico)
        except AcaoNaoAutorizadaException as e:
            print(f"Erro: {e}")
            self.listar_posts(self.controleSistema.topico_atual)