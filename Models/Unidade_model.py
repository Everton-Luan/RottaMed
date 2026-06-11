ARQUIVO = "database/unidades.txt"


# Estrutura os dados da unidade
def criar_dicionario_unidade(nome, tipo, fluxo, especializacoes, cpf, senha):
    return {
        "nome": nome,
        "tipo": tipo,
        "fluxo": fluxo,
        "especializações": especializacoes,
        "cpf_gestor": cpf,
        "senha_gestor": senha
    }

# Salva os dados da unidade no arquivo.txt
def salvar_unidade(unidade):
    with open (ARQUIVO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{unidade['nome']};"
            f"{unidade['tipo']};"
            f"{unidade['fluxo']};"
            f"{unidade['especializações']};"
            f"{unidade['cpf_gestor']};"
            f"{unidade['senha_gestor']}\n"
        )

        arquivo.write(linha)

# Lê os dados de todas as unidades e retorna uma lista de dicionários
def ler_dados_txt():
    # Lê o arquivo e transforma tudo em uma lista de dicionários
    lista_unidades = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) >= 6:
                    unidade = criar_dicionario_unidade(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
                    lista_unidades.append(unidade)
    except FileNotFoundError:
        pass # Se o arquivo não existir, retorna a lista vazia
        
    return lista_unidades