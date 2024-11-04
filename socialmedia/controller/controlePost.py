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
        self.__posts = [Post("Post 1", "Conteúdo do post 1", Admin("admin", "admin"), Topico("Economia")),
                        Post("Post 2", "Conteúdo do post 2", Admin("admin", "admin"), Topico("Tecnologia"))]
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
        usuarioLogado = self.controleSistema.usuarioLogado
        if not isinstance(usuarioLogado, Admin):
            raise AcaoNaoAutorizadaException(
                "Você precisa ser admin para criar um post.")

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
            result = self.post_individual(novo_post)
            return result
        except (AcaoNaoAutorizadaException, EntradaInvalidaException) as e:
            print(f"Erro: {e}")
            self.listar_posts()

    def listar_posts(self, topico=None):
        while True:
            try:
                if not self.controleSistema.usuarioLogado:
                    return "logout"

                topico_posts = self.posts
                if topico:
                    topico_posts = [post for post in self.posts if post.topico.nome == topico.nome]
                    if not topico_posts:
                        print("Nenhum post encontrado para este tópico.")
                        print("Exibindo todos os posts.")
                        self.controleSistema.topico_atual = None
                        topico_posts = self.posts

                escolha = self.telaPost.mostrar_lista_posts(
                    topico_posts,
                    self.controleSistema.topico_atual
                )

                # Handle logout command
                if escolha.lower() == "e":
                    return "logout"

                if not escolha.isdigit():
                    print("Opção inválida. Por favor, digite um número válido ou 'E' para sair.")
                    continue

                escolha = int(escolha)

                if escolha == 1:
                    if self.criar_post() == "logout":
                        return "logout"
                    continue
                elif escolha == 0:
                    return None
                else:
                    indice = escolha - 2
                    if 0 <= indice < len(topico_posts):
                        resultado = self.post_individual(topico_posts[indice])
                        if resultado == "logout":
                            return "logout"
                    else:
                        raise PostNaoEncontradoException("Post não encontrado.")

            except ValueError:
                print("Por favor, digite um número válido.")
            except PostNaoEncontradoException as e:
                print(f"Erro: {e}")
            except EntradaInvalidaException as e:
                print(f"Erro: {e}")

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
            print("Comentário adicionado com sucesso!")
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
                return "logout"
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
            return
        except AcaoNaoAutorizadaException as e:
            print(f"Erro: {e}")