from Views.Menu_view import *
from Utils.Validacoes import *
from Controllers.cidadao_controller import salvar_usuario, listar_upas_proximas
from Views.Cidadao_view import menu_cidadao

menu()

opcao = int(input("\nEscolha uma opção: "))

if opcao == 1:
    entrada = int(input("1.Fazer login\n2.Criar conta\n0.Sair\n"))

    match entrada:
        case 1:
            input("Fazer login com CPF: ")
            input("Digite sua senha: ")
            print("\nLogin realizado com sucesso!")
            
            while True:
                opcao_cidadao = menu_cidadao()
                if opcao_cidadao == "1":
                    print("\nEm desenvolvimento")
                elif opcao_cidadao == "2":
                    print("\nEm desenvolvimento")
                elif opcao_cidadao == "3":
                    listar_upas_proximas()
                elif opcao_cidadao == "4":
                    print("\nSaindo da conta...")
                    break

        case 2:
            nome = input("Nome: ")
            while validar_nome(nome) == False:
                print("Nome inválido.")
                nome = input("Nome: ")
            cpf = input("CPF: ")
            while validar_cpf(cpf) == False:
                print("CPF inválido.")
                cpf = input("CPF: ")
            senha = float(input("Senha: "))
        

            usuario = {
                "nome": nome,
                 "cpf": cpf,
                 "senha": senha
                 }

            salvar_usuario(usuario)
            print("Cadastrado Realizado!")
        case 0:
            print("\nSaindo...")
        case _:
            print("Opção inválida")
