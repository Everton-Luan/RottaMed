def menu_cidadao():
        print("\n" + "=" * 45)
        print(" ROTTAMED ".center(45))
        print("=" * 45)
        print("[1] Visualizar todas unidades ")
        print("[2] Visualizar unidade especifica")
        print("[3] Ver unidades mais próximas (GPS)")
        print("[4] Sair")
        print("=" * 45)

        opcao = input("▶ Escolha uma opção: ").strip()
        while opcao not in ["1", "2", "3"]:
            opcao = input(" ❌ Opção inválida!! Digite novamente: ").strip()
        return opcao

def confirmacao_volta():
    """Pergunta se o usuário tem certeza e devolve True (Sim) ou False (Não)"""
    resposta = input("=" * 45 +"\n[1] Voltar\n[2] Sair\n▶ Escolha uma opção: ").strip()
    while resposta not in ["1", "2"]:
        resposta = input(" ❌ Opção inválida!! Digite novamente: ").strip()

    match resposta:
        case "1":
            return True
        case "2":
            return False
         
def pedir_localizacao_atual():
    print(" \nINFORME SUA LOCALIZAÇÃO\n ")

    print("Você pode digitar o nome da sua rua, bairro ou CEP.")
    endereco = input("▶ Exemplo: 'Rua da Aurora, Recife' ou '50030-000':\n▶ Meu endereço: ").strip()
    return endereco

def exibir_unidades_com_distancia(unidades):
    print(" UNIDADES MAIS PRÓXIMAS ")

    if not unidades:
        print("▶ Nenhuma unidade encontrada.")
    else:
        for i, unidade in enumerate(unidades, start=1):
            dist = unidade.get('distancia_km', 0)
            print(f"\n[{i}] {unidade['nome']} - {dist:.2f} km de distância")
            print(f"   Tipo: {unidade['tipo']}")
            print(f"   Lotação: {unidade['fluxo']}")
            print(f"   Especialidades: {unidade['especializações']}")