ARQUIVO = "database/unidades.txt"


# Estrutura os dados da unidade
def criar_dicionario_unidade(nome, tipo, fluxo, especializacoes, cpf, senha, latitude=0.0, longitude=0.0):
    return {
        "nome": nome,
        "tipo": tipo,
        "fluxo": fluxo,
        "especializações": especializacoes,
        "cpf_gestor": cpf,
        "senha_gestor": senha,
        "latitude": float(latitude),
        "longitude": float(longitude)
    }

# Salva os dados de uma UNICA unidade no arquivo.txt, adicionando-o na ultima linha
def salvar_unidade(unidade):
    with open (ARQUIVO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{unidade['nome']};"
            f"{unidade['tipo']};"
            f"{unidade['fluxo']};"
            f"{unidade['especializações']};"
            f"{unidade['cpf_gestor']};"
            f"{unidade['senha_gestor']};"
            f"{unidade['latitude']};"
            f"{unidade['longitude']}\n"
        )

        arquivo.write(linha)

# Modifica os dados de TODAS as unidades
def modificar_unidades(lista_unidades):
    """Apaga o arquivo atual e reescreve tudo usando a lista fornecida."""
    
    # 🚨 ATENÇÃO: O segredo está na letra "w" (Write/Sobrescrever)
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        
        # Como recebemos uma lista, fazemos um 'for' para gravar uma por uma
        for unidade in lista_unidades:
            linha = (
                f"{unidade['nome']};"
                f"{unidade['tipo']};"
                f"{unidade['fluxo']};"
                f"{unidade['especializações']};"
                f"{unidade['cpf_gestor']};"
                f"{unidade['senha_gestor']};"
                f"{unidade['latitude']};"
                f"{unidade['longitude']}\n"
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
                if len(dados) >= 8: # Agora exigimos estritamente 8 campos
                    unidade = criar_dicionario_unidade(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7])
                    lista_unidades.append(unidade)
    except FileNotFoundError:
        pass # Se o arquivo não existir, retorna a lista vazia
        
    return lista_unidades