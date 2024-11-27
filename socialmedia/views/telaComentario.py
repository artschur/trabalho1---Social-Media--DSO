import PySimpleGUI as sg


class TelaComentario:
    def _init_(self):
        sg.theme('Reddit')
        self.window = None

    def tela_editar_comentario(self):
        layout = [
            [sg.Text("Digite o novo conteúdo do comentário:")],
            [sg.Multiline(size=(50, 3), key='-CONTEUDO-')],
            [sg.Button('Confirmar', key='-CONFIRMAR-'), sg.Button('Cancelar', key='-CANCELAR-')]
        ]

        window = sg.Window('Editar Comentário', layout, modal=True)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, '-CANCELAR-'):
                novo_conteudo = ''
                break
            if event == '-CONFIRMAR-':
                novo_conteudo = values['-CONTEUDO-'].strip()
                break

        window.close()
        return novo_conteudo

    def mostrar_opcoes_comentario(self):
        layout = [
            [sg.Text("Opções do Comentário")],
            [sg.Button('Curtir comentário', key='1', size=(20, 1))],
            [sg.Button('Editar comentário', key='2', size=(20, 1))],
            [sg.Button('Deletar comentário', key='3', size=(20, 1))],
            [sg.Button('Voltar', key='4', size=(20, 1))]
        ]

        window = sg.Window('Opções do Comentário', layout, modal=True)

        event, _ = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, None):
            return '4'
        return event

    def confirmar_delecao(self):
        layout = [
            [sg.Text("Tem certeza que deseja deletar este comentário?")],
            [sg.Button('Sim', key='-SIM-'), sg.Button('Não', key='-NAO-')]
        ]

        window = sg.Window('Confirmar Deleção', layout, modal=True)

        event, _ = window.read()
        window.close()

        return event == '-SIM-'

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem, title='Aviso')