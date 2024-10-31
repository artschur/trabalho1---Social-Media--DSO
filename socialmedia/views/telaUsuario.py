class TelaUsuario:
    def tela_inicial(self):
        print("Bem vindo ao Social Media!")
        print("Escolha uma opção:")
        print("1 - Logar")
        print("2 - Cadastrar")
        print("3 - Sair")
        return input()

    def tela_login(self):
        username = input("Digite seu username: ")
        senha = input("Digite sua senha: ")
        return {"username": username, "senha": senha}

    def tela_cadastro(self):
        print("Tela de cadastro")
        username = input("Digite seu username: ")
        senha = input("Digite sua senha: ")
        return {"username": username, "senha": senha}
