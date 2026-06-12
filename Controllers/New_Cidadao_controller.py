from Models.Unidade_model import ler_dados_txt
from Utils.geolocalizacao import calcular_distancia, endereco_para_coordenadas
from Views.Cidadao_view import pedir_localizacao_atual, exibir_unidades_com_distancia

ARQUIVO = "Database/usuarios.txt"

def salvar_usuario(usuario):

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{usuario['nome']};"
            f"{usuario['cpf']};"
            f"{usuario['senha']}\n;"
        )

        arquivo.write(linha)

def listar_upas_proximas():
    # 1. Pede o endereço do usuário (Texto "Rua..." ou "CEP")
    endereco_digitado = pedir_localizacao_atual()
    
    # Exibe que está processando pois a busca na internet pode levar uns segundos
    print("\nBuscando suas coordenadas, aguarde...")
    
    # 2. Converte o texto para (Latitude, Longitude)
    loc_usuario = endereco_para_coordenadas(endereco_digitado)
    
    if not loc_usuario:
        print(" Não foi possível encontrar este endereço. Tente ser mais específico (Ex: 'Rua X, Cidade').")
        return

    # 3. Busca todas as unidades cadastradas no Model
    unidades = ler_dados_txt()

    # 4. Calcula a distância matemática para cada unidade
    for unidade in unidades:
        loc_upa = (unidade['latitude'], unidade['longitude'])
        # Usa a nossa função geopy que criamos
        distancia = calcular_distancia(loc_usuario, loc_upa)
        unidade['distancia_km'] = distancia

    # 5. Ordena a lista pelas unidades que têm a menor distância
    unidades_ordenadas = sorted(unidades, key=lambda u: u['distancia_km'])

    # 6. Envia as unidades ordenadas para a View mostrar na tela
    exibir_unidades_com_distancia(unidades_ordenadas)

