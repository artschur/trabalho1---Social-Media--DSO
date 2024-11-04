from socialmedia.controller.controleSistema import ControleSistema

if __name__ == "__main__":
    sis = ControleSistema()

    while True:
        print("Bem vindo ao SocialBlogs!\nFaça login ou cadastre-se para continuar. Nos somos uma rede social baseada em tópicos.")
        user = sis.telainit()

        if user is None or "user" not in user:
            print("Login falhou. Tente novamente.")
            continue
        print(f"Bem-vindo, {user['user'].username}!")
        sis.usuarioLogado = user["user"]

        while sis.usuarioLogado:  # Inner loop for logged-in user session
            topico_selecionado = sis.controleTopico.get_topico()
            if topico_selecionado is None:
                continue

            sis.topico_atual = topico_selecionado
            result = sis.controlePost.listar_posts(sis.topico_atual)

            # Handle logout from the posts listing
            if result == "logout":
                sis.logout()
                break  # Break inner loop to return to login screen