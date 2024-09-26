from comentario import Comentario


class CommentManager:
    def comentar(self, comentario: Comentario, post: "Post"):
        if post is not None:  # comentario.autor.ncommentpost <= 3:
            post.adicionar_comentario(comentario)
        else:
            raise ValueError("Post não existe.")
