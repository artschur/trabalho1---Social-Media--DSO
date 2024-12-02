import PySimpleGUI as sg


class TelaUsuario:
    def __init__(self):
        sg.theme('Reddit')

    def tela_inicial(self):
        layout = [
            [sg.Text("Bem-vindo!", font=('Helvetica', 24), justification='center')],
            [sg.Button('Login', key='1', size=(20, 2), font=('Helvetica', 16))],
            [sg.Button('Cadastro', key='2', size=(20, 2), font=('Helvetica', 16))],
            [sg.Button('Ver relatórios', key='R', size=(20, 2), font=('Helvetica', 16))],
            [sg.Button('Sair', key='3', size=(20, 2), font=('Helvetica', 16))]
        ]

        window = sg.Window('Sistema', layout, element_justification='center', finalize=True, size=(600, 600))
        event, _ = window.read()
        window.close()

        return event if event not in (sg.WIN_CLOSED, None) else '3'

    def tela_login(self):
        layout = [
            [sg.Text("Login", font=('Helvetica', 20), justification='center')],
            [sg.Text("Username:", font=('Helvetica', 14))],
            [sg.Input(key='-USERNAME-', size=(30, 1), font=('Helvetica', 14))],
            [sg.Text("Senha:", font=('Helvetica', 14))],
            [sg.Input(key='-SENHA-', password_char='*', size=(30, 1), font=('Helvetica', 14))],
            [sg.Button('Entrar', key='-LOGIN-', size=(15, 1), font=('Helvetica', 14)),
             sg.Button('Cancelar', key='-CANCELAR-', size=(15, 1), font=('Helvetica', 14))]
        ]

        window = sg.Window('Login', layout, element_justification='center', finalize=True, size=(600, 600))
        event, values = window.read()

        result = None
        if event == '-LOGIN-':
            result = {
                "username": values['-USERNAME-'].strip(),
                "senha": values['-SENHA-'].strip()
            }

        window.close()
        return result

    def tela_cadastro(self):
        layout = [
            [sg.Text("Cadastro de Usuário", font=('Helvetica', 20), justification='center')],
            [sg.Text("Username:", font=('Helvetica', 14))],
            [sg.Input(key='-USERNAME-', size=(30, 1), font=('Helvetica', 14))],
            [sg.Text("Senha:", font=('Helvetica', 14))],
            [sg.Input(key='-SENHA-', password_char='*', size=(30, 1), font=('Helvetica', 14))],
            [sg.Text("Você é um administrador?", font=('Helvetica', 14))],
            [sg.Radio('Sim', 'ADMIN', key='-ADMIN_SIM-', font=('Helvetica', 14)),
             sg.Radio('Não', 'ADMIN', key='-ADMIN_NAO-', default=True, font=('Helvetica', 14))],
            [sg.Button('Cadastrar', key='-CADASTRAR-', size=(15, 1), font=('Helvetica', 14)),
             sg.Button('Cancelar', key='-CANCELAR-', size=(15, 1), font=('Helvetica', 14))]
        ]

        window = sg.Window('Cadastro', layout, element_justification='center', default_element_size=23,finalize=True, size=(600, 600))
        event, values = window.read()

        result = None
        if event == '-CADASTRAR-':
            result = {
                "username": values['-USERNAME-'].strip(),
                "senha": values['-SENHA-'].strip(),
                "admin": 's' if values['-ADMIN_SIM-'] else 'n'
            }

        window.close()
        return result