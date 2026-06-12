import unicodedata

def remover_acentos(texto):
    #Normalize é uma função que vai separar os caracteres dos seus acentos 
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    
    #Aqui vai voltar o texto sem acentos 
    texto_sem_acento = "".join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    
    return texto_sem_acento