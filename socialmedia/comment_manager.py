from post import Post
from usuario import Usuario


class CommentManager:
    def comentar(self, conteudo_comentario: str, post: Post, autor: Usuario):
        if post is not None:
            post.adicionar_comentario(conteudo_comentario, autor)
        else:
            raise ValueError("Post não existe.")
