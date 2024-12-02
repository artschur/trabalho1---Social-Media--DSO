import PySimpleGUI as sg


class TelaPost:
    def __init__(self):
        sg.theme('Reddit')

    def tela_criar_post(self, lista_topicos):
        layout = [
            [sg.Text("Criar Novo Post", font=('Helvetica', 14))],
            [sg.Text("Título do post:")],
            [sg.Input(key='-TITULO-', size=(50, 1))],
            [sg.Text("Conteúdo do post:")],
            [sg.Multiline(key='-CONTEUDO-', size=(50, 10))],
            [sg.Text("Selecione o Tópico:")],
            [sg.Combo([topico.nome for topico in lista_topicos], key='-TOPICO-', size=(30, 1))],
            [sg.Button('Criar Post', key='-CRIAR-'), sg.Button('Cancelar', key='-CANCELAR-')]
        ]

        window = sg.Window('Criar Post', layout, modal=True, size=(600, 600))

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, '-CANCELAR-'):
                window.close()
                return None

            if event == '-CRIAR-':
                titulo = values['-TITULO-'].strip()
                conteudo = values['-CONTEUDO-'].strip()
                topico_escolhido = values['-TOPICO-']

                if not all([titulo, conteudo, topico_escolhido]):
                    sg.popup("Todos os campos devem ser preenchidos!", title="Erro")
                    continue

                topico = next((t for t in lista_topicos if t.nome == topico_escolhido), None)
                window.close()
                return {"titulo": titulo, "conteudo": conteudo, "topico": topico}

    def mostrar_lista_posts(self, posts, topico=None):
        header = f"Lista de Posts - {topico.nome if topico else 'Todos os Posts'}"

        post_list = [[sg.Text(header, font=('Helvetica', 20))]]
        if not posts:
            post_list.append([sg.Text("Nenhum post encontrado")])

        post_list.extend([
            [sg.Button('Criar Post', key='1', size=(30, 2))],
            [sg.Text("Posts:", font=('Helvetica', 16))],
        ])

        for i, post in enumerate(posts, 2):
            post_list.append([sg.Button(f"{post.titulo}", key=str(i), size=(30, 2), font=('Helvetica', 16))])

        post_list.extend([
            [sg.Text("")],
            [sg.Button('Voltar', key='0'), sg.Button('Logout', key='E')]
            ])


        window = sg.Window('Lista de Posts', post_list, modal=True, size=(600, 600), element_justification='center')
        event, _ = window.read()
        window.close()

        return event if event not in (sg.WIN_CLOSED, None) else '0'

    def mostrar_comentarios(self, post):
        layout = [
            [sg.Text("Comentários", font=('Helvetica', 16))],
            *[[sg.Text(f"{i}. '{c.conteudo}' - {c.autor.username} | {c.count_likes} likes",
                       font=('Helvetica', 16))]
              for i, c in enumerate(post.comentarios, 1)],
            [sg.Text("")],
            [sg.Button('Interagir com Comentário', key='1'), sg.Button('Voltar', key='2')]
        ]

        window = sg.Window('Comentários', layout, modal=True, resizable=True, size=(600, 600),element_justification='center')
        event, _ = window.read()
        window.close()

        return "voltar" if event in (sg.WIN_CLOSED, '2') else event

    def selecionar_comentario(self, post):
        layout = [
            [sg.Text("Selecione o comentário para interagir:", font=('Helvetica', 16))],
            *[[sg.Button(f"{i}. '{c.conteudo}' - {c.autor.username} | {c.count_likes} likes",
                         key=str(i), size=(50, 1))]
              for i, c in enumerate(post.comentarios, 1)],
            [sg.Button('Voltar', key='-VOLTAR-')]
        ]

        window = sg.Window('Selecionar Comentário', layout, modal=True, size=(600, 600))
        event, _ = window.read()
        window.close()

        return event if event not in (sg.WIN_CLOSED, '-VOLTAR-') else None

    def comentar_post(self):
        layout = [
            [sg.Text("Digite seu comentário:")],
            [sg.Multiline(size=(50, 5), key='-COMENTARIO-')],
            [sg.Button('Enviar', key='-ENVIAR-'), sg.Button('Cancelar', key='-CANCELAR-')]
        ]

        window = sg.Window('Comentar Post', layout, modal=True, size=(600, 600))
        event, values = window.read()
        comentario = values['-COMENTARIO-'].strip() if event == '-ENVIAR-' else ''
        window.close()

        return comentario

    def vizualizar_post(self, post):
        layout = [
            [sg.Text(f"{post.titulo} - {post.autor.username}", font=('Helvetica', 18),
                     justification='center', expand_x=True)],
            [sg.Text(f"Tópico: {post.topico.nome}", font=('Helvetica', 14), justification='center',
                     expand_x=True)],
            [sg.Multiline(post.conteudo, size=(50, 10), disabled=True, font=('Helvetica', 12),
                          justification='center', expand_x=True)],
            [sg.Text(f"{post.count_likes()} likes | {post.count_comentarios()} comentários",
                     font=('Helvetica', 14), justification='center', expand_x=True)],
            [sg.Button('Curtir post', key='1', size=(20, 2), font=('Helvetica', 14))],
            [sg.Button('Comentar', key='2', size=(20, 2), font=('Helvetica', 14))],
            [sg.Button('Ver comentários', key='3', size=(20, 2), font=('Helvetica', 14))],
            [sg.Button('Voltar', key='4', size=(20, 2), font=('Helvetica', 14))]
        ]

        centered_layout = [[sg.Column(layout, element_justification='center',
                                      justification='center', expand_x=True, expand_y=True)]]

        window = sg.Window(
            'Visualizar Post',
            centered_layout,
            modal=True,
            resizable=True,
            size=(600, 600),
            element_justification='center'
        )
        event, _ = window.read()
        window.close()

        return event if event not in (sg.WIN_CLOSED, None) else '4'