from usuario import Usuario
from post import Post
from app import Aplicativo


class Admin(Usuario):
    def __init__(self, username: str, email: str, senha: str):
        super().__init__(username=username, email=email, senha=senha)

    def postar(self, post, topico):
        conteudo = "teste"
        novoPost = Post(
            conteudo=conteudo, autor=self
        )  # setando autor como o proprio admin que postou

        if topico in Aplicativo().topicos:
            topico.posts.append(novoPost)
        else:
            return "Seção não encontrada"
