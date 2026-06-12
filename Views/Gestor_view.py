
def menu_gestor():
    print("\n" + "=" * 45)
    print(" GESTÃO DO PLANTÃO ".center(45))
    print("=" * 45)
    print("[1] Atualizar Especialidades")
    print("[2] Atualizar Fluxo")
    print("[3] Visualizar Painel Geral")
    print("[4] Sair")
    print("=" * 45)

    return input("▶ Escolha uma opção: ").strip()


def pedir_especialidades():
    print("\n" + "=" * 45)
    print(" ATUALIZAR ESPECIALIDADES ".center(45))
    print("=" * 45)

    especialidades = input(
        "▶ Digite as especialidades da unidade: "
    ).strip().title()

    return especialidades


def pedir_lotacao():
    print("\n" + "=" * 45)
    print(" ATUALIZAR FLUXO ".center(45))
    print("=" * 45)

    lotacao = input(
        "▶ Digite a nova lotação da unidade: "
    ).strip()

    return lotacao


def exibir_painel_geral(unidade):
    print("\n" + "=" * 45)
    print(" PAINEL GERAL DA UNIDADE ".center(45))
    print("=" * 45)

    print(f"▶ Nome: {unidade['nome']}")
    print(f"▶ Tipo: {unidade['tipo']}")
    print(f"▶ Fluxo: {unidade['fluxo']}")
    print(f"▶ Especialidades: {unidade['especializações']}")
    print(f"▶ Lotação: {unidade['lotacao']}")

    print("=" * 45 + "\n")