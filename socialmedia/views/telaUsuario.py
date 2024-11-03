class TelaUsuario:
    def tela_inicial(self):
        print("Bem vindo ao SocialBlogs!")
        print("Faça login ou cadastre-se para continuar. Nos somos uma rede social baseada em tópicos.")
        print("Escolha uma opção:")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Sair")
        return input()

    def tela_login(self):
        username = input("Digite seu username: ")
        senha = input("Digite sua senha: ")
        return {"username": username, "senha": senha}

    def tela_cadastro(self):
        print("Bem vindo a tela de cadastro!")
        username = input("Digite seu username: ")
        senha = input("Digite sua senha: ")
        return {"username": username, "senha": senha}
        
