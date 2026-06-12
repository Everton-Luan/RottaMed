import Views.Cidadao_view as viewC
import Controllers.Unidade_controller as controllU
from Models.Unidade_model import ler_dados_txt
from Utils.geolocalizacao import calcular_distancia, endereco_para_coordenadas
from Views.Cidadao_view import pedir_localizacao_atual, exibir_unidades_com_distancia
import Controllers.Rottinha_controller as controllChat

def iniciar_tela_cidadao(): 
    while True:
        # 1. Chama a tela que você acabou de me mostrar
        opcao = viewC.menu_cidadao()

        match opcao:
            case "1":
                print("\n" + "=" * 45)
                print("\n📋 [VISUALIZANDO TODAS AS UNIDADES]")
                print("\n" + "=" * 45)
                # Aqui chamamos a função de listagem geral que você já tem pronta
                controllU.iniciar_busca_geral() 
                if viewC.confirmacao_volta():
                    continue
                else:
                    print("Saindo...")
                    break

            case "2":
                print("\n" + "=" * 45)
                print("\n🔍 [BUSCAR UNIDADE ESPECÍFICA]")
                print("\n" + "=" * 45)
                # Aqui chamamos a função de busca por nome que você já tem pronta
                controllU.iniciar_busca_especifica() 
                if viewC.confirmacao_volta():
                    continue
                else:
                    print("Saindo...")
                    break
            case "3":
                print("\n" + "=" * 45)
                print("\n📍 [BUSCANDO UNIDADES PRÓXIMAS]")
                print("\n" + "=" * 45)
                
                # 1. Pede o endereço ao cidadão
                endereco = viewC.pedir_localizacao_atual()
                coordenadas = endereco_para_coordenadas(endereco)
                
                if coordenadas:
                    # 2. Lê todas as unidades do arquivo
                    lista = ler_dados_txt()
                    
                    # 3. Calcula a distância para cada uma
                    unidades_com_dist = []
                    for unidade in lista:
                        coord_unidade = (float(unidade['latitude']), float(unidade['longitude']))
                        distancia = calcular_distancia(coordenadas, coord_unidade)
                        
                        # Adiciona a distância ao dicionário da unidade
                        unidade['distancia_km'] = distancia
                        unidades_com_dist.append(unidade)
                    
                    # 4. Ordena pela mais próxima
                    unidades_com_dist.sort(key=lambda x: x['distancia_km'])
                    
                    # 5. Exibe as 3 mais próximas (ou todas se tiver menos de 3)
                    viewC.exibir_unidades_com_distancia(unidades_com_dist[:3])
                else:
                    print("\n Não foi possível encontrar a localização informada.")
                
                if viewC.confirmacao_volta():
                    continue
                else:
                    print("Saindo...")
                    break
        
            case "4":
                print("\n" + "=" * 45)
                print("\n [ROTINHA]")
                print("\n" + "=" * 45)
                controllChat.iniciar_chatbot()

            case "5":
                print("\n" + "=" * 45)
                print("\n↩️ Retornando ao Menu Principal...")
                print("\n" + "=" * 45)
                break # Quebra o

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
