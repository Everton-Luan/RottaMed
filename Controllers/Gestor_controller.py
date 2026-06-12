import Models.Unidade_model as modelU 
import Views.Unidade_view as viewU
import Views.Gestor_view as viewG

def iniciar_tela_gestor():
    #Pede as credenciais do Gestor
    cpf_digitado, senha_digitada = viewG.pedir_credenciais()
    
    #Carrega todo o banco de dados na memória
    lista_unidades = modelU.ler_dados_txt()
    
    #Variáveis para guardar o login do usuário
    unidade_logada = None
    indice_logado = -1
    
    #Busca o CPF e a Senha a partir dos dados existentes no dicionário
    for i, u in enumerate(lista_unidades):
        if u["cpf_gestor"] == cpf_digitado and u["senha_gestor"] == senha_digitada:
            unidade_logada = u
            indice_logado = i
            break #Após encontrar, para o for.
            
    #Caso não encontre, não permite a entrada na área do gestor
    if unidade_logada is None:
        print("\n Login falhou: CPF ou senha incorretos ou não cadastrados.")
        return #O usuário retorna ao menu 
        
    print(f"\n Acesso liberado! Bem-vindo(a) gestor(a) da {unidade_logada['nome'].title()}.")
    
    #O laço infinito de navegação do gestor
    while True:
        opcao = viewG.menu_gestor(unidade_logada["nome"])
        
        match opcao:
            case "1":
            
                viewU.exibir_unidade_unica(unidade_logada)
                
            case "2":
                
                unidade_logada = iniciar_atualizacao_gestor(unidade_logada, indice_logado, lista_unidades)         

            case "3":
                print("\n Fazendo logout... Retornando ao Menu Principal.")
                break #Quebra o while



def iniciar_atualizacao_gestor(unidade, indice, lista_unidades):
    
    #Aparece na view para o gestor atualizar os dados
    novo_fluxo, nova_espec = viewU.gestor_atualiza_dados(unidade)

    #é trocado essas duas chaves lá no dicionário
    unidade["fluxo"] = novo_fluxo
    unidade["especializações"] = nova_espec
    
    #A lista principal é atualizada
    lista_unidades[indice] = unidade
    
    #O Model salva a lista nova
    modelU.modificar_unidades(lista_unidades)
    
    print("\n Fluxo e Especializações atualizados com sucesso!")
    
    return unidade