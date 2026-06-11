from Views.Unidade_view import *

ARQUIVO =  "database/unidades.txt"

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

def cadastrar_unidade():
    # 1. Chama a View para pegar os dados
    nome, tipo, fluxo, espec, cpf, senha = add_dados_unidade()
    
    # 2. Empacota
    unidade_dict = {
        "nome": nome,
        "tipo": tipo,
        "fluxo": fluxo,
        "especializações": espec,
        "cpf_gestor": cpf,
        "senha_gestor": senha
    }
    
    # 3. Salva
    salvar_unidade(unidade_dict)
    menssagem("Unidade cadastrada com sucesso!!")

def ler_unidade():
    pass
  