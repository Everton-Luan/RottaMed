import Utils.Validacoes as utilV
import Utils.texto as utilT
import textwrap

#Pegando os dados que digitou
def add_dados_unidade():
    print("\n===== Adicionando dados da unidade =====")

    nome = input("▶ Digite o nome da unidade: ").strip().title()
    while utilV.validar_nome(nome) == False:
        nome = input("Nome inválido!! digite novamente: ")

    tipo = input("▶ Digite o tipo (UPA/UBS): ").strip().upper()
    while tipo not in ["UPA", "UBS"]:
        tipo = input("Tipo inválido!! digite UPA ou UBS: ").strip().upper()

    fluxo = input("▶ Digite o fluxo: ").strip().title()

    espec = input("▶ Digite as especializações: ").strip().title()

    cpf_gestor = input("▶ Digite o CPF do gestor: ").strip()
    while utilV.validar_cpf(cpf_gestor) == False:
            cpf_gestor = input("CPF inválido!! Digite novamente: ")

    senha_gestor = input("▶ Digite a senha do gestor: ")

    print("\n Localização da Unidade:")

    latitude = utilV.pedir_coordenada("▶ Digite a Latitude (ex: -8.0475): ")

    longitude = utilV.pedir_coordenada("▶ Digite a Longitude (ex: -34.8770): ")
    
    return nome, tipo, fluxo, espec, cpf_gestor, senha_gestor, latitude, longitude

def gestor_atualiza_dados(unidade):
    print("\n" + "="*45)
    print(" ATUALIZANDO DADOS DA UNIDADE ".center(45))
    print("="*45)
    texto = ("Caso não queira modificar algum dado, apenas aperte enter.")
    texto_formatado = textwrap.fill(
            texto,
            width=45,
            subsequent_indent="  " #Dá dois espacinhos se a palavra tiver que descer
        )
    print(texto_formatado)
    print("-" * 45)

    #Mostra os dados da unidade antes de atualizar
    exibir_unidade_unica(unidade)

    #Pede o novo fluxo
    print(" Atualizar dados:")
    print("-" * 45)
    novo_fluxo = input("▶ Novo Fluxo: ").strip()
    # Se o usuário apertar Enter vazio, mantemos o que já estava
    if novo_fluxo == "":
        novo_fluxo = unidade['fluxo']
        
    #Pede as novas especializações
    nova_espec = input("▶ Novas Especializações: ").strip()
    # Se apertar Enter vazio, mantemos as antigas
    if nova_espec == "":
        nova_espec = unidade['especializações']
        
    return novo_fluxo, nova_espec


#Perguntas
def pedir_nome_busca():
    print("\n===== Buscar unidade específica =====")
    nome = input("▶ Digite o nome da Unidade: ")
    return nome

# Mostra todas as unidades
def exibir_unidades(lista_unidades):
    if not lista_unidades: # Se a lista estiver vazia
        print("\n Nenhuma unidade cadastrada ainda.")
        return

    print("\n" + "="*45)
    print(" LISTA GERAL DE UNIDADES DE SAÚDE ".center(45))
    print("="*45)
    
    for i, unidade in enumerate(lista_unidades):
        #Mostra a primeira linha (Nome e Tipo)
        print(f"[{i + 1}] {unidade['nome'].title()} ({unidade['tipo']})")
        #Mostra a segunda linha (Fluxo)
        print(f"▶ Fluxo: {unidade['fluxo']}")
        #Mostra a linha de especializações
        texto_espec = f"▶ Especializações: {unidade['especializações'].title()}"
        #O textwrap vai agir só nas especializações se passar de 45 letras
        texto_espec_formatado = textwrap.fill(
            texto_espec,
            width=45,
            subsequent_indent="  " #Dá dois espacinhos se a palavra tiver que descer
        )
        #Mostra a linha de especializações formatada
        print(texto_espec_formatado)
        print(f"▶ Latitude: {unidade['latitude']}")
        print(f"▶ Longitude: {unidade['longitude']}")
    
        # Linha divisória de baixo
        print("-" * 45)

#Mostra uma unidade
def exibir_unidade_unica(unidade):
    if unidade is None:
        print("\n Unidade não encontrada no sistema.")
        return

    print("\n" + "="*45)
    print(f" UNIDADE: {unidade['nome'].title()} ".center(45))
    print("="*45)
    print(f"▶ Tipo: {unidade['tipo']}")
    print(f"▶ Fluxo Atual: {unidade['fluxo']}")
    texto_espec = f"▶ Especializações: {unidade['especializações'].title()}"
    texto_espec_formatado = textwrap.fill(
            texto_espec,
            width=45,
            subsequent_indent="  " #Dá dois espacinhos se a palavra tiver que descer
        )
    print(texto_espec_formatado)
    print(f"▶ Latitude: {unidade['latitude']}")    
    print(f"▶ Longitude: {unidade['longitude']}")

    print("="*45 + "\n")

def confirmacao_exclusao():
    """Pergunta se o usuário tem certeza e devolve True (Sim) ou False (Não)"""
    resposta = input(" Tem certeza que deseja excluir esta unidade permanentemente? (Sim/Não): ").strip().upper()
    resposta = utilT.remover_acentos(resposta)
    while resposta not in ["SIM", "NAO"]:
        resposta = input(" Tipo inválido!! digite 'Sim' ou 'Não'!!: ").strip().upper()

    match resposta:
        case "SIM":
            return True
        case "NAO":
            return False


def menssagem(m):
     print(m)
