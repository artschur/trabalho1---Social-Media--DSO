from usuario import Usuario


class Admin(Usuario):
    def __init__(self, username: str, email: str, senha: str):
        super().__init__(username=username, email=email, senha=senha)

    def postar(self, conteudo, topico_name):

        from post import Post
        from app import Aplicativo

        novoPost = Post(
            conteudo=conteudo,
            autor=self,  # setando autor como o proprio admin que postou
        )

        for topico in Aplicativo().topicos:
            if topico.name == topico_name:
                topico.adicionar_post(novoPost)
                return novoPost
        return "topico nao encontrado"

    def deletar_post(self, post):
        assert isinstance(post, post.Post)
        from app import Aplicativo

        for topico in Aplicativo().topicos:
            if post in topico.posts:
                topico.posts.remove(post)
                return "Post deleted"
        return "Post not found"


arthur = Admin("arthur", "teste", "teste")
arthur.login()

print(arthur.postar("teste", "Tecnologia").conteudo)
