import Models.Unidade_model as model
import Views.Unidade_view as view
import Utils.Menssagem as util

ARQUIVO =  "database/unidades.txt"

# Parte do Create

# Criando unidade
def iniciar_cadastro_unidade():
    # Chama a View para pegar os dados da nova unidade 
    nome, tipo, fluxo, espec, cpf, senha = view.add_dados_unidade()
    
    # Estrutura os dados recebidos em um dicionario usando o model para serem padronizados
    nova_unidade = model.criar_dicionario_unidade(nome, tipo, fluxo, espec, cpf, senha)
    
    # Salva
    model.salvar_unidade(nova_unidade)
    util.menssagem(" ✅ Unidade cadastrada com sucesso!!")

# Parte do Read

# 1. Lê e imprime TODAS as unidades
def iniciar_busca_geral():
    # Pega todas as unidades cadastradas
    todas_as_unidades = model.ler_dados_txt()
    
    # Manda a View mostrar a lista inteira
    view.exibir_unidades(todas_as_unidades)


# 2. Lê e imprime uma UNICA unidade
def iniciar_busca_especifica():
    # Pede para a View perguntar o nome
    nome_procurado = view.pedir_nome_busca().upper()
    
    # Pega todas as unidades do TXT
    todas_as_unidades = model.ler_dados_txt()
    
    # Faz uma busca: se achar o nome, guarda a unidade e para de procurar
    unidade_encontrada = None
    for u in todas_as_unidades:
        if u["nome"].upper() == nome_procurado:
            unidade_encontrada = u
            break 
            
    # Manda a View mostrar o resultado (pode ser a unidade ou um aviso de erro)
    view.exibir_unidade_unica(unidade_encontrada)
  