from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def calcular_distancia(coord_origem, coord_destino):
    #Vai receber latitude e longitude e converte para km.
    return geodesic(coord_origem, coord_destino).kilometers

def endereco_para_coordenadas(endereco):
    #Recebe um endereço ou CEP e retorna latitude e longitude
    try:
        #Tem que identificar quem ta fazendo a API
        geolocator = Nominatim(user_agent="rottamed_app_busca_upas")
        
        #O timeout é para não travar na internet ruim
        location = geolocator.geocode(endereco, timeout=10)
        
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except (GeocoderTimedOut, GeocoderServiceError):
        #Se não conseguir se conectar com a API
        return None