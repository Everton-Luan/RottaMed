def menu_dev():
    print("\n" + "=" * 45)
    print(" GESTÃO DESENVOLVEDOR ".center(45))
    print("=" * 45)
    print("[1] Cadastrar Unidade")
    print("[2] Visualizar Unidades")
    print("[3] Atualizar Unidade")
    print("[4] Deletar Unidade")
    print("[5] Sair")
    print("=" * 45)

    opcao = input("▶ Escolha uma opção: ").strip()
    while opcao not in ["1","2", "3", "4","5"]:
        opcao = input(" ❌ Opção inválida!! Digite novamente: ").strip()
    return opcao

def pedir_dados_unidade():
    print("\n" + "=" * 45)
    print(" CADASTRAR UNIDADE ".center(45))
    print("=" * 45)

    nome = input("▶ Nome da unidade: ").strip().title()
    tipo = input("▶ Tipo da unidade: ").strip().title()
    fluxo = input("▶ Fluxo da unidade: ").strip().title()
    especializacoes = input("▶ Especialidades da unidade: ").strip().title()
    cpf_gestor = input("▶ CPF do gestor da unidade: ").strip()
    senha_gestor = input("▶ Senha do gestor: ").strip()
    latitude = input("▶ Latitude da unidade (ex: -8.128555): ").strip()
    longitude = input("▶ Longitude da unidade (ex: -34.949972): ").strip()

    return {
        "nome": nome,
        "tipo": tipo, 
        "fluxo": fluxo,
        "especializações": especializacoes,
        "cpf_gestor": cpf_gestor,
        "senha_gestor": senha_gestor,
        "latitude": latitude,
        "longitude": longitude
    }


def exibir_unidades(unidades):
    print("\n" + "=" * 45)
    print(" LISTA DE UNIDADES ".center(45))
    print("=" * 45)

    if not unidades:
        print("▶ Nenhuma unidade cadastrada.")
    else:
        for i, unidade in enumerate(unidades, start=1):
            print(f"\n[{i}] {unidade['nome']}")
            print(f"   Tipo: {unidade['tipo']}")
            print(f"   Fluxo: {unidade['fluxo']}")
            print(f"   Especialidades: {unidade['especializações']}")
            print(f"   Lotação: {unidade['lotacao']}")

    print("\n" + "=" * 45)


def pedir_unidade_atualizacao():
    print("\n" + "=" * 45)
    print(" ATUALIZAR UNIDADE ".center(45))
    print("=" * 45)

    return input(
        "▶ Digite o nome da unidade que deseja atualizar: "
    ).strip().title()


def pedir_novos_dados():
    print("\n" + "=" * 45)
    print(" NOVOS DADOS ".center(45))
    print("=" * 45)

    tipo = input("▶ Novo tipo: ").strip().title()
    fluxo = input("▶ Novo fluxo: ").strip()
    especializacoes = input("▶ Nova lotação: ").strip()

    return{
        "tipo": tipo, 
        "fluxo": fluxo,
        "especializações": especializacoes,
    }


def pedir_unidade_exclusao():
    print("\n" + "=" * 45)
    print(" DELETAR UNIDADE ".center(45))
    print("=" * 45)

    return input(
        "▶ Digite o nome da unidade que deseja deletar: "
    ).strip().title()


def confirmar_exclusao(nome):
    resposta = input(
        f"▶ Tem certeza que deseja deletar '{nome}': (S/N): "
    ).strip().upper()

    return resposta == "S"


def exibir_mensagem(mensagem):
    print("\n" + "=" * 45)
    print(f"▶ {mensagem}")
    print("=" * 45)