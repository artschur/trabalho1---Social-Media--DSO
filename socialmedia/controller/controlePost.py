from socialmedia.post import Post
from socialmedia.topico import Topico

class ControlePost:
    def __init__(self, controladorSistema):
        self.__lista_posts = []
        self.__controleSistema = controladorSistema

    def criar_post(self):
        usuario_logado = self.__controleSistema.usuario_logado
        if not usuario_logado:
            self.__tela_post.mostrar_mensagem("Você precisa estar logado para criar um post")
            return
        dados_post = self.__tela_post.tela_criar_post()
        if dados_post['titulo'] and dados_post['conteudo']:
            topico = self.obter_topico_por_nome(dados_post['topico'])
            novo_post = Post(dados_post['titulo'], dados_post['conteudo'], usuario_logado, topico)
            self.__lista_posts.append(novo_post)
            self.__tela_post.mostrar_mensagem("Post criado com sucesso")
        else:
            self.__tela_post.mostrar_mensagem("Erro ao criar post")
        

    def obter_topico_por_nome(self, nome_topico: str):
        return Topico(nome_topico)
    
    def listar_posts(self):
        while True:    
            escolha = self._tela_post.mostrar_lista_post(self.__lista_posts)
            if escolha == "0":
                break
            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(self.__lista_posts):
                    self.visualizar_post(self.__lista_posts[indice])
                else:
                    self.__tela_post.mostrar_mensagem("Escolha Inválida")
            except ValueError:
                self.__tela_post.mostrar_mensagem("Digite um número válido")
                



