from socialmedia.post import Post
from socialmedia.comentario import Comentario
from socialmedia.views.telaComentario import TelaComentario
from socialmedia.admin import Admin

class ControleComentario:
    def __init__(self, controleSistema):
        self.__comentarios = []
        self.__controleSistema = controleSistema
        self.__telaComentario = TelaComentario()

    @property
    def comentarios(self):
        return self.__comentarios

    @property
    def telaComentario(self):
        return self.__telaComentario

    def adicionar_comentario(self, post: Post, conteudo: str) -> Comentario:
        if not self.__controleSistema.usuarioLogado:
            self.telaComentario.mostrar_mensagem("Você precisa estar logado para comentar.")
            return None

        if not conteudo.strip():
            self.telaComentario.mostrar_mensagem("O comentário não pode estar vazio.")
            return None

        novo_comentario = Comentario(conteudo, self.__controleSistema.usuarioLogado)
        post.comentarios.append(novo_comentario)
        self.__comentarios.append(novo_comentario)
        return novo_comentario

    def editar_comentario(self, comentario: Comentario) -> bool:
        if not self.__controleSistema.usuarioLogado:
            self.telaComentario.mostrar_mensagem("Você precisa estar logado para editar um comentário.")
            return False

        if self.__controleSistema.usuarioLogado != comentario.autor:
            self.telaComentario.mostrar_mensagem("Você não tem permissão para editar este comentário.")
            return False

        novo_conteudo = self.telaComentario.tela_editar_comentario()
        if not novo_conteudo:
            return False

        comentario.conteudo = novo_conteudo
        return True

    def curtir_comentario(self, comentario: Comentario) -> bool:
        if not self.__controleSistema.usuarioLogado:
            self.telaComentario.mostrar_mensagem("Você precisa estar logado para curtir um comentário.")
            return False

        usuario = self.__controleSistema.usuarioLogado
        if usuario in comentario.likes:
            comentario.likes.remove(usuario)
            self.telaComentario.mostrar_mensagem("Curtida removida")
        else:
            comentario.likes.append(usuario)
            self.telaComentario.mostrar_mensagem("Comentário curtido")
        return True

    def deletar_comentario(self, comentario: Comentario, post: Post) -> bool:
        if not self.__controleSistema.usuarioLogado:
            self.telaComentario.mostrar_mensagem("Você precisa estar logado para deletar um comentário.")
            return False

        if self.__controleSistema.usuarioLogado != comentario.autor:
            self.telaComentario.mostrar_mensagem("Você não tem permissão para deletar este comentário.")
            return False

        if self.telaComentario.confirmar_delecao():
            post.comentarios.remove(comentario)
            self.__comentarios.remove(comentario)
            self.telaComentario.mostrar_mensagem("Comentário deletado")
            return True
        return False

    def gerenciar_comentario(self, comentario: Comentario, post: Post):
        opcao = self.telaComentario.mostrar_opcoes_comentario()

        if opcao == "1":
            return self.curtir_comentario(comentario)
        elif opcao == "2":
            return self.editar_comentario(comentario)
        elif opcao == "3":
            return self.deletar_comentario(comentario, post)
        elif opcao == "4":
            return False
        else:
            self.telaComentario.mostrar_mensagem("Opção inválida!")
            return False