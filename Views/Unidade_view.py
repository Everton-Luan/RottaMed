from Utils.Validacoes import *

def menssagem(m):
     print(m)

def add_dados_unidade():
    nome = input("- Digite o nome da unidade: ")
    while validar_nome(nome) == False:
        nome = input("- Nome inválido!! digite novamente: ")

    tipo = input("- Digite o tipo (UPA/UBS): ").upper()
    while tipo not in ["UPA", "UBS"]:
        tipo = input("- Tipo inválido!! digite UPA ou UBS: ").upper()

    fluxo = input("- Digite o fluxo: ")

    espec = input("- Digite as especializações: ")

    cpf_gestor = input("- Digite o CPF do gestor: ")
    while validar_cpf(cpf_gestor) == False:
            cpf_gestor = input("- CPF inválido!! Digite novamente: ")

    senha_gestor = input("- Digite a senha do gestor: ")

    return nome, tipo, fluxo, espec, cpf_gestor, senha_gestor