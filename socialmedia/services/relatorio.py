import PySimpleGUI as sg
from socialmedia.daos.dao_post import PostsDAO
from socialmedia.daos.dao_topico import TopicosDAO

class Relatorio:
    def __init__(self, controle_post):
        self.__controle_post = controle_post
        self.__postsDAO = PostsDAO()
        self.__topicosDAO = TopicosDAO()
        sg.theme('Reddit')

    def mostrar_relatorios(self):
        post_curtido = self.__get_post_mais_curtido()
        topico_posts = self.__get_topico_mais_posts()
        topico_interacoes = self.__get_topico_mais_interacoes()
        autor = self.__get_autor_mais_curtido()

        layout = [
            [sg.Text("Relatórios do Sistema", font=('Helvetica', 20, 'bold'),
                     justification='center', expand_x=True, pad=(0, 20))],


            [sg.Frame("Post Mais Curtido", [
                [sg.Text(self.__format_post_curtido(post_curtido), key='-POST-',
                         font=('Helvetica', 14), size=(60, 15))]
            ], font=('Helvetica', 18), size=(800, 100))],


            [sg.Frame("Tópico com Mais Posts", [
                [sg.Text(self.__format_topico_posts(topico_posts), key='-TOPICO-',
                         font=('Helvetica', 14), size=(60, 15))]
            ], font=('Helvetica', 18), size=(800, 100))],


            [sg.Frame("Tópico com Mais Interações", [
                [sg.Text(self.__format_topico_interacoes(topico_interacoes), key='-INTERACOES-',
                         font=('Helvetica', 14), size=(60, 15))]
            ], font=('Helvetica', 18), size=(800, 100))],


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
        posts = self.__postsDAO.get_all()
        if not posts:
            return None

        for post in posts:
            if not hasattr(post, 'likes'):
                post.likes = []

        try:
            post_mais_curtido = max(posts, key=lambda post: len(post.likes))
            return (post_mais_curtido, len(post_mais_curtido.likes)) if post_mais_curtido else None
        except ValueError:
            return None

    def __get_topico_mais_posts(self):
        topicos = self.__topicosDAO.get_all()
        posts = self.__postsDAO.get_all()
        if not topicos or not posts:
            return None

        try:
            count_post_por_topico = {}
            for topico in topicos:
                posts_topico = [post for post in posts if post.topico.id == topico.id]
                count_post_por_topico[topico] = len(posts_topico)

            if not count_post_por_topico:
                return None

            return max(count_post_por_topico.items(), key=lambda x: x[1])
        except Exception as e:
            print(f"Error in __get_topico_mais_posts: {e}")
            return None

    def __get_topico_mais_interacoes(self):
        topicos = self.__topicosDAO.get_all()
        posts = self.__postsDAO.get_all()
        if not topicos or not posts:
            return None

        try:
            interacoes_por_topico = {}
            for topico in topicos:
                posts_topico = [post for post in posts if post.topico.id == topico.id]
                interacoes = sum(
                    len(getattr(post, 'likes', [])) +
                    len(getattr(post, 'comentarios', []))
                    for post in posts_topico
                )
                interacoes_por_topico[topico] = interacoes

            if not interacoes_por_topico:
                return None

            return max(interacoes_por_topico.items(), key=lambda x: x[1])
        except Exception as e:
            print(f"Error in __get_topico_mais_interacoes: {e}")
            return None

    def __get_autor_mais_curtido(self):
        posts = self.__postsDAO.get_all()
        if not posts:
            return None

        try:
            curtidas_por_autor = {}
            for post in posts:
                if hasattr(post, 'autor') and hasattr(post, 'likes'):
                    autor = post.autor
                    curtidas = len(post.likes)
                    curtidas_por_autor[autor] = curtidas_por_autor.get(autor, 0) + curtidas

            if not curtidas_por_autor:
                return None

            return max(curtidas_por_autor.items(), key=lambda x: x[1])
        except Exception:
            return None

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
        result = self.__get_post_mais_curtido()
        return f"Post mais curtido: {result[0].titulo} - {result[1]} curtidas" if result else "Sem posts"

    def topico_com_mais_posts(self):
        result = self.__get_topico_mais_posts()
        return f"Tópico com mais posts: {result[0].nome} - {result[1]} posts" if result else "Sem tópicos"

    def topico_com_mais_interacoes(self):
        result = self.__get_topico_mais_interacoes()
        return f"Tópico com mais interações: {result[0].nome} - {result[1]} interações" if result else "Sem tópicos"

    def autor_mais_curtido(self):
        result = self.__get_autor_mais_curtido()
        return f"Autor mais curtido: {result[0].username} - {result[1]} curtidas" if result else "Sem autores"