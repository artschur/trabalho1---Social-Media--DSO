class TelaUsuario:
    def tela_inicial(self):
        print("Escolha uma opção:")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Sair")
        print("R - Ver relatorios")
        return input()

    def tela_login(self):
        username = input("Digite seu username: ")
        senha = input("Digite sua senha: ")
        return {"username": username, "senha": senha}

    def tela_cadastro(self):
        print("Bem vindo a tela de cadastro!")
        username = input("Digite seu username: ")
        senha = input("Digite sua senha: ")
        admin = input("Você é um administrador? (S/N): ").strip().lower()
        return {"username": username, "senha": senha, "admin": admin}
        
