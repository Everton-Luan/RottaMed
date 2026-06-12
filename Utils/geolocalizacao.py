from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def calcular_distancia(coord_origem, coord_destino):
    #Recebe tuplas de (latitude, longitude) e retorna a distância em km.
    return geodesic(coord_origem, coord_destino).kilometers

def endereco_para_coordenadas(endereco):
    #Recebe um endereço de texto ou CEP e retorna a tupla (latitude, longitude).
    #Retorna None se não conseguir encontrar.
    try:
        # Nominatim exige um 'user_agent' identificando quem está fazendo a API
        geolocator = Nominatim(user_agent="rottamed_app_busca_upas")
        
        # O timeout evita que o programa trave se a internet estiver lenta
        location = geolocator.geocode(endereco, timeout=10)
        
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except (GeocoderTimedOut, GeocoderServiceError):
        # Em caso de falha de conexão com a API
        return None