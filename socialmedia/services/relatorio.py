class Relatorio:
    def __init__(self, controle_post):
        self.__controle_post = controle_post

    def post_mais_curtido(self):
        if not self.__controle_post.posts:
            print('Nenhum post cadastrado')
            return None

        post_mais_curtido = None
        maior_qtd_curtidas = -1
        for post in self.__controle_post.posts:
            if len(post.likes) > maior_qtd_curtidas:
                post_mais_curtido = post
                maior_qtd_curtidas = len(post.likes)

        if post_mais_curtido:
            print(f'Post mais curtido: {post_mais_curtido.titulo} , com {maior_qtd_curtidas} curtidas. Feito por {post_mais_curtido.autor.username} \n')
            return post_mais_curtido

    def topico_com_mais_posts(self):
        if not self.__controle_post.posts:
            print('Nenhum post cadastrado')
            return None
        count_post_por_topico = {}
        for post in self.__controle_post.posts:
            if post.topico.nome not in count_post_por_topico:
                topico = post.topico
                if topico in count_post_por_topico:
                    count_post_por_topico[topico] += 1
                else:
                    count_post_por_topico[topico] = 1
        topico_mais_popular = None
        maior_qtd_posts = -1

        for topico, contagem in count_post_por_topico.items():
            if contagem > maior_qtd_posts:
                topico_mais_popular = topico
                maior_qtd_posts = contagem

        if topico_mais_popular:
            print(f'Topico com mais posts: {topico_mais_popular.nome} , com {maior_qtd_posts} posts \n')
            return topico_mais_popular
        else:
            print('Nenhum post cadastrado')
            return None

    def topico_com_mais_interacoes(self):
        if not self.__controle_post.posts:
            print('Nenhum post cadastrado')
            return None

        interacoes_por_topico = {}
        for post in self.__controle_post.posts:
            topico = post.topico
            interacoes = len(post.likes) + len(post.comentarios)
            if topico in interacoes_por_topico:
                interacoes_por_topico[topico] += interacoes
            else:
                interacoes_por_topico[topico] = interacoes

        topico_mais_interacoes = None
        maior_qtd_interacoes = -1

        for topico, interacoes in interacoes_por_topico.items():
            if interacoes > maior_qtd_interacoes:
                topico_mais_interacoes = topico
                maior_qtd_interacoes = interacoes

        if topico_mais_interacoes:
            print(f'Tópico com mais interações: {topico_mais_interacoes.nome} , com {maior_qtd_interacoes} interações \n')
            return topico_mais_interacoes
        else:
            print('Nenhum post cadastrado')
            return None

    def autor_mais_curtido(self):
        if not self.__controle_post.posts:
            print('Nenhum post cadastrado')
            return None

        curtidas_por_autor = {}
        for post in self.__controle_post.posts:
            autor = post.autor
            curtidas = len(post.likes)
            if autor in curtidas_por_autor:
                curtidas_por_autor[autor] += curtidas
            else:
                curtidas_por_autor[autor] = curtidas

        autor_mais_curtido = None
        maior_qtd_curtidas = -1

        for autor, curtidas in curtidas_por_autor.items():
            if curtidas > maior_qtd_curtidas:
                autor_mais_curtido = autor
                maior_qtd_curtidas = curtidas

        if autor_mais_curtido:
            print(f'Autor mais curtido: {autor_mais_curtido.username} , com {maior_qtd_curtidas} curtidas \n')
            return autor_mais_curtido
        else:
            print('Nenhum post cadastrado')
            return None