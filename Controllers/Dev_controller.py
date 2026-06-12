import Views.Dev_view as viewDev
import Views.Unidade_view as viewU
import Models.Unidade_model as modelU
import Controllers.Unidade_controller as controlU 

def iniciar_tela_dev():
    senha_digitada = viewDev.pedir_senha_master()
    senha_correta = "dev123" 
    
    if senha_digitada != senha_correta:
        print("\n Acesso Negado: Senha master incorreta.")
        return 
        
    print("\n Acesso liberado! Bem-vindo(a) ao painel de controle mestre.")
    
    while True:
        opcao = viewDev.menu_dev()
        
        match opcao:
            case "1": 
                controlU.iniciar_cadastro_unidade()
                
            case "2": 
                lista_unidades = modelU.ler_dados_txt()
                viewU.exibir_unidades(lista_unidades)
                
            case "3": 
                nome_busca = viewU.pedir_nome_busca().upper()
                lista_unidades = modelU.ler_dados_txt()
                
                unidade_encontrada = None
                for u in lista_unidades:
                    if u["nome"].upper() == nome_busca:
                        unidade_encontrada = u
                        break
                        
                viewU.exibir_unidade_unica(unidade_encontrada)
                
            case "4": 
                controlU.iniciar_atualizacao()
                
            case "5": 
                controlU.iniciar_exclusao()
                
            case "6":
                print("\n Encerrando sessão do Desenvolvedor...")
                break