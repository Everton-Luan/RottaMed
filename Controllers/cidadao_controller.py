import Views.Cidadao_view as viewC
import Controllers.Unidade_controller as controllU


def iniciar_tela_cidadao(): 
    while True:
        # 1. Chama a tela que você acabou de me mostrar
        opcao = viewC.menu_cidadao()

        match opcao:
            case "1":
                print("\n" + "=" * 45)
                print("\n📋 [VISUALIZANDO TODAS AS UNIDADES]")
                print("\n" + "=" * 45)
                # Aqui chamamos a função de listagem geral que você já tem pronta
                controllU.iniciar_busca_geral() 
                if viewC.confirmacao_volta():
                    continue
                else:
                    print("Saindo...")
                    break

            case "2":
                print("\n" + "=" * 45)
                print("\n🔍 [BUSCAR UNIDADE ESPECÍFICA]")
                print("\n" + "=" * 45)
                # Aqui chamamos a função de busca por nome que você já tem pronta
                controllU.iniciar_busca_especifica() 
                if viewC.confirmacao_volta():
                    continue
                else:
                    print("Saindo...")
                    break

            case "3":
                print("\n" + "=" * 45)
                print("\n↩️ Retornando ao Menu Principal...")
                print("\n" + "=" * 45)
                break # Quebra o