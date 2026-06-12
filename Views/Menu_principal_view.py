def exibir_menu_principal():
    print("\n" + "="*45)
    print(" SISTEMA ROTTAMED - MENU PRINCIPAL")
    print("="*45)
    print("  [1] - Sou cidadão")
    print("  [2] - Sou gestor")
    print("  [3] - Sou desenvolvedor")
    print("  [4] - Sair do Sistema")
    print("="*45)
    
    opcao = input("▶ Escolha uma opção: ").strip()
    while opcao not in ["1", "2", "3", "4"]:
        opcao = input(" Opção inválida!! Digite novamente: ").strip()

    return opcao

def confirmacao_volta():
    """Pergunta se o usuário quer voltar a tela que estava ou sair"""
    resposta = input("=" * 45 +"\n[1] Voltar\n[2] Sair\n▶ Escolha uma opção: ").strip()
    while resposta not in ["1", "2"]:
        resposta = input("Opção inválida!! Digite novamente: ").strip()

    match resposta:
        case "1":
            return True
        case "2":
            return False