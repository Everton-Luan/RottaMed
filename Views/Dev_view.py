def pedir_senha_master():
    print("\n" + "="*45)
    print(" 👨‍💻 ACESSO RESTRITO - DESENVOLVEDOR ".center(45))
    print("="*45)
    
    senha = input("▶ Digite a senha master: ").strip()
    return senha

def menu_dev():
    print("\n" + "="*45)
    print(" 🛠️ PAINEL DO DESENVOLVEDOR ".center(45))
    print("="*45)
    print("  [1] Cadastrar nova unidade")
    print("  [2] Listar todas as unidades")
    print("  [3] Buscar unidade específica")
    print("  [4] Atualizar dados de uma unidade")
    print("  [5] Excluir uma unidade")
    print("  [6] Sair")
    print("="*45)
    
    opcao = input("▶ Escolha uma opção: ").strip()
    while opcao not in ["1", "2", "3", "4", "5", "6"]:
        opcao = input(" ❌ Opção inválida!! Digite novamente: ").strip()
        
    return opcao