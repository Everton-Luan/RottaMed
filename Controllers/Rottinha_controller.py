import Views.Rottinha_view as viewChat

def iniciar_chatbot():
    viewChat.exibir_boas_vindas()
    
    while True:
        # Puxa a pergunta da View
        resposta = viewChat.perguntar_gravidade()
        
        match resposta:
            case "1":
                # Respondeu que é grave -> UPA
                viewChat.exibir_resultado("UPA")
            case "2":
                # Respondeu que é leve/rotina -> UBS
                viewChat.exibir_resultado("UBS")
            case "3":
                print("\nEncerrando.")
                break
       
        #Pergunta se o usuário quer fazer uma nova triagem ou sair
        print("\nDeseja fazer outra consulta com o Rottinha?")
        print("[1] Sim")
        print("[2] Não")
        continuar = input("▶ Escolha uma opção: ").strip()
        
        # Validação para garantir que o usuário só digite 1 ou 2
        while continuar not in ["1", "2"]:
            continuar = input(" Opção inválida!! Digite 1 ou 2: ").strip()
            
        if continuar == "2":
            print("\nRetornando ao menu anterior...")
            break