from socialmedia.exceptions.exceptions import (

    PostNaoEncontradoException,
    ComentarioNaoEncontradoException,
    AcaoNaoAutorizadaException,
    EntradaInvalidaException
)
from socialmedia.post import Post
from socialmedia.views.telaPost import TelaPost
from socialmedia.admin import Admin
from socialmedia.controller.controleComentario import ControleComentario
from socialmedia.daos.dao_post import PostsDAO
from socialmedia.controller.controleTopicos import ControleTopico

class ControlePost:
    def __init__(self, controladorSistema, controleTopicos: ControleTopico):
        self.__controleSistema = controladorSistema
        self.__telaPost = TelaPost()
        self.__controleTopicos = controleTopicos
        self.__controleComentario = ControleComentario(controladorSistema)
        self.__dao = PostsDAO()

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
    def controleComentario(self):
        return self.__controleComentario

    @property
    def dao(self):
        return self.__dao

    def usuario_e_admin(self):
        usuarioLogado = self.controleSistema.usuarioLogado
        if not isinstance(usuarioLogado, Admin):
            raise AcaoNaoAutorizadaException(
                "Você precisa ser admin para criar um post.")

    def criar_post(self):
        try:
            self.usuario_e_admin()
            dados_post = self.__telaPost.tela_criar_post(self.controleTopicos.dao.get_all())
            if not (dados_post['titulo'] and dados_post['conteudo']):
                raise EntradaInvalidaException("Erro: Título ou conteúdo do post está faltando.")

            topico_escolhido = dados_post['topico']
            if not topico_escolhido:
                raise EntradaInvalidaException("Tópico inválido.")

            novo_post = Post(dados_post['titulo'], dados_post['conteudo'],
                             self.__controleSistema.usuarioLogado, topico_escolhido)
            self.dao.adicionarPost(novo_post)
            return self.post_individual(novo_post)

        except (AcaoNaoAutorizadaException, EntradaInvalidaException) as e:
            print(f"Erro: {e}")
            return None

    def listar_posts(self, topico=None):
        while True:
            try:
                if not self.controleSistema.usuarioLogado:
                    return "logout"

                topico_posts = self.dao.get_all()
                if topico:
                    topico_posts = [post for post in self.dao.get_all() if
                                    post.topico.nome == topico.nome]
                    if not topico_posts:
                        print("Nenhum post encontrado para este tópico.")
                        print("Exibindo todos os posts.")
                        self.controleSistema.topico_atual = None
                        topico_posts = list(self.dao.get_all())

                escolha = self.telaPost.mostrar_lista_posts(
                    topico_posts,
                    self.controleSistema.topico_atual
                )

                if escolha.lower() == "e":
                    return "logout"

                if not escolha.isdigit():
                    raise EntradaInvalidaException("Escolha inválida.")
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
                        continue
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
            comentario = self.controleComentario.adicionar_comentario(post, conteudo)
            if comentario:
                print("Comentário adicionado com sucesso!")

        except EntradaInvalidaException as e:
            print(f"Erro: {e}")
            self.listar_posts(self.controleSistema.topico_atual)

    def interage_comentarios(self, post):
        try:
            if not post.comentarios:
                print("Este post ainda não tem comentários.")
                return

            escolha = self.telaPost.mostrar_comentarios(post)
            if escolha == "voltar":
                return

            if escolha == "1":
                indice_comentario = int(self.telaPost.selecionar_comentario(post)) - 1
                if 0 <= indice_comentario < len(post.comentarios):
                    comentario = post.comentarios[indice_comentario]
                    resposta =  self.controleComentario.gerenciar_comentario(comentario, post)
                    if not resposta:
                        return self.listar_posts(self.controleSistema.topico_atual)
                    return resposta

                else:
                    raise ComentarioNaoEncontradoException("Comentário não encontrado.")
            else:
                print("Escolha inválida")
                self.listar_posts(self.controleSistema.topico_atual)
        except ValueError:
            raise EntradaInvalidaException("Escolha inválida.")
        except ComentarioNaoEncontradoException as e:
            raise ComentarioNaoEncontradoException("Comentário não encontrado.")

    def post_individual(self, post):
        while True:
            try:
                escolha = int(self.telaPost.vizualizar_post(post))
                acoes_com_post = {1: self.curtir_post, 2: self.comentar,
                                  3: self.interage_comentarios}

                if escolha in acoes_com_post:
                    acoes_com_post[escolha](post)
                elif escolha == 4:
                    return None
                else:
                    raise EntradaInvalidaException("Escolha inválida")
            except (ValueError, EntradaInvalidaException) as e:
                raise EntradaInvalidaException()

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