def pedir_credenciais():
    print("\n" + "="*45)
    print(" 🔐 LOGIN DO GESTOR ".center(45))
    print("="*45)

    cpf = input("▶ Digite seu CPF: ").strip()
    senha = input("▶ Digite sua senha: ").strip()

    return cpf, senha

def menu_gestor(nome_unidade):
    print("\n" + "="*45)
    print(" 🏥 PAINEL DO GESTOR ".center(45))
    print(f" 📍 {nome_unidade} ".center(45))
    print("="*45)
    print("  [1] Visualizar dados da minha unidade")
    print("  [2] Atualizar Fluxo e Especializações")
    print("  [3] Sair")
    print("="*45)

    opcao = input("▶ Escolha uma opção: ").strip()
    while opcao not in ["1", "2", "3"]:
        opcao = input(" ❌ Opção inválida!! Digite novamente: ").strip()

    return opcao