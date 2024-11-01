from socialmedia.post import Post
from socialmedia.topico import Topico
from socialmedia.views.telaPost import TelaPost
class NotLoggedInError(Exception):
    pass

class PostCreationError(Exception):
    pass

class ControlePost:
    def __init__(self, controladorSistema):
        self.__lista_posts = []
        self.__controleSistema = controladorSistema
        self.__telaPost = TelaPost()
        self.__lista_topicos = ["Economia", "Tecnologia", "Esportes"]


    @property
    def telaPost(self):
        return self.__telaPost

    @property
    def lista_posts(self):
        return self.__lista_posts

    @property
    def lista_topicos(self):
        return self.__lista_topicos

    def criar_post(self):
        usuario_logado = self.__controleSistema.usuario_logado
        if not usuario_logado:
            self.telaPost.mostrar_mensagem("Você precisa estar logado para criar um post")
            return False

        try:
            dados_post = self.__telaPost.tela_criar_post(self.lista_topicos)
            if dados_post['titulo'] and dados_post['conteudo']:
                topico = self.obter_topico_por_nome(dados_post['topico'])
                novo_post = Post(dados_post['titulo'], dados_post['conteudo'], usuario_logado, topico)
                self.lista_posts.append(novo_post)
                return True
            else:
                raise PostCreationError("Erro: Título ou conteúdo do post está faltando.")
        except PostCreationError as e:
            self.telaPost.mostrar_mensagem(str(e))
            return False
    def obter_topico_por_nome(self, nome_topico: str):
        return Topico(nome_topico)

    def listar_posts(self):
        while True:
            escolha = self.__telaPost.mostrar_lista_posts(self.__lista_posts)
            if escolha == "0":
                break
            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(self.__lista_posts):
                    self.telaPost.vizualizar_post(self.__lista_posts[indice])
                else:
                    raise IndexError("Escolha Inválida")
            except ValueError:
                raise ValueError("Escolha Inválida")
            except IndexError as e:
                raise IndexError(str(e))