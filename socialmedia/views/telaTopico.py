import PySimpleGUI as sg


class TelaTopico:
    def __init__(self):
        sg.theme('Reddit')

    def obter_nome_topico(self):
        layout = [
            [sg.Text("Digite o nome do novo tópico:", font=('Helvetica', 14), justification='center', expand_x=True)],
            [sg.Input(key='-NOME-', size=(40, 4), font=('Helvetica', 16))],
            [sg.Button('Confirmar', key='-CONFIRMAR-', size=(12, 4), font=('Helvetica', 16)),
             sg.Button('Cancelar', key='-CANCELAR-', size=(12, 4), font=('Helvetica', 16))]
        ]

        window = sg.Window('Novo Tópico', layout, modal=True, size=(600, 200), resizable=True, element_justification='center')
        event, values = window.read()
        nome = values['-NOME-'].strip() if event == '-CONFIRMAR-' else ''
        window.close()

        return nome

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem, title='Aviso', font=('Helvetica', 16))

    def mostrar_lista_topicos(self, topicos):
        layout = [
            [sg.Text("Lista de Tópicos", font=('Helvetica', 16, 'bold'), justification='center', expand_x=True, pad=(0, 20))],
            *[[sg.Button(f"{topico.nome}", key=str(i), size=(30, 1), font=('Helvetica', 16))]
              for i, topico in enumerate(topicos, 1)],
            [sg.Text("", size=(1, 1))],
            [sg.Button('Adicionar novo tópico', key='0', size=(20, 1), font=('Helvetica', 16))],
            [sg.Button('Sair', key='e', size=(10, 1), font=('Helvetica', 16))]
        ]

        window = sg.Window('Tópicos', layout, modal=True, size=(600, 400), resizable=True, element_justification='center')
        event, _ = window.read()
        window.close()

        return event if event not in (sg.WIN_CLOSED, None) else 'e'

    def adicionar_topico(self):
        layout = [
            [sg.Text("Adicionar Novo Tópico", font=('Helvetica', 16, 'bold'), justification='center', expand_x=True, pad=(0, 20))],
            [sg.Text("Digite o nome do novo tópico:", font=('Helvetica', 14), justification='center', expand_x=True)],
            [sg.Input(key='-NOME-', size=(40, 1), font=('Helvetica', 16))],
            [sg.Button('Adicionar', key='-CONFIRMAR-', size=(12, 1), font=('Helvetica', 16)),
             sg.Button('Cancelar', key='-CANCELAR-', size=(12, 1), font=('Helvetica', 16))]
        ]

        window = sg.Window('Adicionar Tópico', layout, modal=True, size=(500, 300), resizable=True, element_justification='center')
        event, values = window.read()
        nome = values['-NOME-'].strip() if event == '-CONFIRMAR-' else ''
        window.close()

        return nome