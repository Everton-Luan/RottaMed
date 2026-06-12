def menu_cidadao():
        print("\n" + "=" * 45)
        print(" ROTTAMED ".center(45))
        print("=" * 45)
        print("[1] Visualizar todas unidades ")
        print("[2] Visualizar unidade especifica")
        print("[3] Sair")
        print("=" * 45)

        opcao = input("▶ Escolha uma opção: ").strip()
        while opcao not in ["1", "2", "3"]:
            opcao = input(" ❌ Opção inválida!! Digite novamente: ").strip()
        return opcao