import Views.Menu_principal_view as viewM
import Controllers.cidadao_controller as controllerC
import Controllers.Gestor_controller as controllerG

def iniciar_sistema():
    while True:
        #Puxa a sua função que exibe a tela e devolve 1, 2, 3 ou 4
        opcao = viewM.exibir_menu_principal()

        match opcao:
            case "1":
                # Direciona o usuário para o laço do Cidadão que acabamos de fazer!
                controllerC.iniciar_tela_cidadao()
                
            case "2":
            
                controllerG.iniciar_tela_gestor()
            
            case "3":
                print("\n" + "=" * 45)
                print(" 🚧 TELA DESENVOLVEDOR (Em desenvolvimento) 🚧".center(45))
                print("=" * 45)
                if viewM.confirmacao_volta():
                    continue
                else:
                    print("Saindo...")
                    break
                # No futuro:
                # controllerD.iniciar_tela_dev()
                
            case "4":
                print("\n" + "=" * 45)
                print(" 👋 Encerrando o sistema RottaMed... Até logo!".center(45))
                print("=" * 45)
                break # Quebra o while principal, desligando o programa

#Essa condição garante que o sistema só rode se este arquivo for executado diretamente
if __name__ == "__main__":
    iniciar_sistema()

