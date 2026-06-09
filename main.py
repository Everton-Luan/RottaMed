from Views.Menu_view import *
from Utils.Validacoes import *
from Controllers.cidadao_controller import salvar_usuario

menu()

opcao = int(input("\nEscolha uma opção: "))
if opcao == 1:
    entrada = int(input("1.Fazer login\n2.Criar conta\n"))
    if entrada == 1:
        print("ok")

    elif entrada ==2:
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

elif opcao == 2:
    input("Fazer login com CPF: ")
    input("Digite sua senha: ")

