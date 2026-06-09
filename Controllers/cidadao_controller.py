ARQUIVO = "Database/usuarios.txt"


def salvar_usuario(usuario):

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{usuario['nome']};"
            f"{usuario['cpf']};"
            f"{usuario['senha']};"
        )

        arquivo.write(linha)