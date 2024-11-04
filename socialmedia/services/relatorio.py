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
            print(f'Post mais curtido: {post_mais_curtido}')
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
            print(f'Topico com mais posts: {topico_mais_popular}')
            return topico_mais_popular
        else:
            print('Nenhum post cadastrado')
            return None
        