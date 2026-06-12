import unicodedata

def remover_acentos(texto):
    """Transforma 'NÃO' em 'NAO', 'Saúde' em 'Saude', etc."""
    # O normalize 'NFKD' separa os caracteres dos seus acentos (o 'a' do 'tilde')
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    
    # Esta linha reconstrói o texto apenas com as letras, jogando os acentos fora
    texto_sem_acento = "".join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    
    return texto_sem_acento