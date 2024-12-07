import PySimpleGUI as sg


class Relatorio:
    def __init__(self, controle_post):
        self.__controle_post = controle_post
        sg.theme('Reddit')

    def mostrar_relatorios(self):
        post_curtido = self.__get_post_mais_curtido()
        topico_posts = self.__get_topico_mais_posts()
        topico_interacoes = self.__get_topico_mais_interacoes()
        autor = self.__get_autor_mais_curtido()

        layout = [
            [sg.Text("Relatórios do Sistema", font=('Helvetica', 20, 'bold'),
                     justification='center', expand_x=True, pad=(0, 20))],

            # Post mais curtido
            [sg.Frame("Post Mais Curtido", [
                [sg.Text(self.__format_post_curtido(post_curtido), key='-POST-',
                         font=('Helvetica', 14), size=(60, 15))]
            ], font=('Helvetica', 18), size=(800, 100))],

            # Tópico com mais posts
            [sg.Frame("Tópico com Mais Posts", [
                [sg.Text(self.__format_topico_posts(topico_posts), key='-TOPICO-',
                         font=('Helvetica', 14), size=(60, 15))]
            ], font=('Helvetica', 18), size=(800, 100))],

            # Tópico com mais interações
            [sg.Frame("Tópico com Mais Interações", [
                [sg.Text(self.__format_topico_interacoes(topico_interacoes), key='-INTERACOES-',
                         font=('Helvetica', 14), size=(60, 15))]
            ], font=('Helvetica', 18), size=(800, 100))],

            # Autor mais curtido
            [sg.Frame("Autor Mais Curtido", [
                [sg.Text(self.__format_autor_curtido(autor), key='-AUTOR-', font=('Helvetica', 14),
                         size=(60, 3))]
            ], font=('Helvetica', 18), size=(800, 100))],

            [sg.Button('Fechar', key='-CLOSE-', size=(12, 1), font=('Helvetica', 14))]
        ]

        window = sg.Window(
            'Relatórios',
            layout,
            modal=True,
            size=(900, 600),
            resizable=True
        )
        while True:
            event, _ = window.read()
            if event == sg.WINDOW_CLOSED or event == '-CLOSE-':
                window.close()
                break

    def __get_post_mais_curtido(self):
        if not self.__controle_post.posts:
            return None

        post_mais_curtido = None
        maior_qtd_curtidas = -1
        for post in self.__controle_post.posts:
            if len(post.likes) > maior_qtd_curtidas:
                post_mais_curtido = post
                maior_qtd_curtidas = len(post.likes)

        return (post_mais_curtido, maior_qtd_curtidas) if post_mais_curtido else None

    def __get_topico_mais_posts(self):
        if not self.__controle_post.posts:
            return None

        count_post_por_topico = {}
        for post in self.__controle_post.posts:
            if post.topico.nome not in count_post_por_topico:
                topico = post.topico
                if topico in count_post_por_topico:
                    count_post_por_topico[topico] += 1
                else:
                    count_post_por_topico[topico] = 1

        if not count_post_por_topico:
            return None

        return max(count_post_por_topico.items(), key=lambda x: x[1])

    def __get_topico_mais_interacoes(self):
        if not self.__controle_post.posts:
            return None

        interacoes_por_topico = {}
        for post in self.__controle_post.posts:
            topico = post.topico
            interacoes = len(post.likes) + len(post.comentarios)
            if topico in interacoes_por_topico:
                interacoes_por_topico[topico] += interacoes
            else:
                interacoes_por_topico[topico] = interacoes

        if not interacoes_por_topico:
            return None

        return max(interacoes_por_topico.items(), key=lambda x: x[1])

    def __get_autor_mais_curtido(self):
        if not self.__controle_post.posts:
            return None

        curtidas_por_autor = {}
        for post in self.__controle_post.posts:
            autor = post.autor
            curtidas = len(post.likes)
            if autor in curtidas_por_autor:
                curtidas_por_autor[autor] += curtidas
            else:
                curtidas_por_autor[autor] = curtidas

        if not curtidas_por_autor:
            return None

        return max(curtidas_por_autor.items(), key=lambda x: x[1])

    # Formatting methods
    def __format_post_curtido(self, data):
        if not data:
            return "Nenhum post cadastrado"
        post, curtidas = data
        return f"Título: {post.titulo}\nCurtidas: {curtidas}\nAutor: {post.autor.username}"

    def __format_topico_posts(self, data):
        if not data:
            return "Nenhum post cadastrado"
        topico, quantidade = data
        return f"Tópico: {topico.nome}\nQuantidade de Posts: {quantidade}"

    def __format_topico_interacoes(self, data):
        if not data:
            return "Nenhum post cadastrado"
        topico, interacoes = data
        return f"Tópico: {topico.nome}\nTotal de Interações: {interacoes}"

    def __format_autor_curtido(self, data):
        if not data:
            return "Nenhum post cadastrado"
        autor, curtidas = data
        return f"Username: {autor.username}\nTotal de Curtidas: {curtidas}"

    def post_mais_curtido(self):
        return self.__get_post_mais_curtido()

    def topico_com_mais_posts(self):
        return self.__get_topico_mais_posts()

    def topico_com_mais_interacoes(self):
        return self.__get_topico_mais_interacoes()

    def autor_mais_curtido(self):
        self.mostrar_relatorios()