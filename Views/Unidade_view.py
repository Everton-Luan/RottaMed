import Utils.Validacoes as util
import textwrap

# Parte do Create

# 1. Pegando os dados que  serão digitados
def add_dados_unidade():
    print("\n===== Adicionando dados da unidade =====")

    nome = input("▶ Digite o nome da unidade: ").strip().title()
    while util.validar_nome(nome) == False:
        nome = input(" ❌ Nome inválido!! digite novamente: ")

    tipo = input("▶ Digite o tipo (UPA/UBS): ").strip().upper()
    while tipo not in ["UPA", "UBS"]:
        tipo = input(" ❌ Tipo inválido!! digite UPA ou UBS: ").upper()

    fluxo = input("▶ Digite o fluxo: ").strip().title()

    espec = input("▶ Digite as especializações: ").strip().title()

    cpf_gestor = input("▶ Digite o CPF do gestor: ").strip()
    while util.validar_cpf(cpf_gestor) == False:
            cpf_gestor = input(" ❌ CPF inválido!! Digite novamente: ")

    senha_gestor = input("▶ Digite a senha do gestor: ")

    return nome, tipo, fluxo, espec, cpf_gestor, senha_gestor



# Parte do Read

# 1. Ferramenta de pergunta
def pedir_nome_busca():
    print("\n===== Buscar unidade específica =====")
    nome = input("▶ Digite o nome da Unidade: ")
    return nome

# 2. Ferramenta para mostrar TODAS as unidades
def exibir_unidades(lista_unidades):
    if not lista_unidades: # Se a lista estiver vazia
        print("\n❌ Nenhuma unidade cadastrada ainda.")
        return

    print("\n" + "="*45)
    print(" 📋 LISTA GERAL DE UNIDADES DE SAÚDE ".center(45))
    print("="*45)
    
    for i, unidade in enumerate(lista_unidades):
        # Imprime a primeira linha (Nome e Tipo)
        print(f"[{i + 1}] {unidade['nome'].title()} ({unidade['tipo']})")
        
        # Imprime a segunda linha (Fluxo)
        print(f"▶ Fluxo: {unidade['fluxo']}")
        
        # Monta APENAS a linha de especializações
        texto_espec = f"▶ Especializações: {unidade['especializações'].title()}"
        
        # O textwrap vai agir só nas especializações se passar de 45 letras
        texto_espec_formatado = textwrap.fill(
            texto_espec,
            width=45,
            subsequent_indent="  " # Dá dois espacinhos se a palavra tiver que descer
        )
        
        # Imprime a linha de especializações formatada
        print(texto_espec_formatado)
        
        # Linha divisória de baixo
        print("-" * 45)

# 3. Ferramenta para mostrar UMA unidade
def exibir_unidade_unica(unidade):
    if unidade is None:
        print("\n❌ Unidade não encontrada no sistema.")
        return

    print("\n" + "="*45)
    print(f" 🏥 UNIDADE: {unidade['nome'].title()} ".center(45))
    print("="*45)
    print(f"▶ Tipo: {unidade['tipo']}")
    print(f"▶ Fluxo Atual: {unidade['fluxo']}")
    texto_espec = f"▶ Especializações: {unidade['especializações'].title()}"
    texto_espec_formatado = textwrap.fill(
            texto_espec,
            width=45,
            subsequent_indent="  " # Dá dois espacinhos se a palavra tiver que descer
        )
    print(texto_espec_formatado)
    print("="*45 + "\n")