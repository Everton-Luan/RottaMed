import re

def validar_cpf(cpf: str) -> bool:
    # Extraindo apenas os números do CPF
    cpf_limpo = re.sub(r'\D', '', cpf)

    # Conferindo se o tamanho está correto
    if len(cpf_limpo) != 11:
        return False

    # Conferindo se todos os dígitos são iguais (ex: 111.111.111-11)
    # Se a string inteira for igual ao primeiro dígito repetido 11x, é inválido
    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    # Convertendo a string para uma lista de inteiros
    cpf_array = [int(digito) for digito in cpf_limpo]

    # Validação do primeiro dígito
    soma1 = 0
    multiplicador1 = 10
    for i in range(9):
        soma1 += cpf_array[i] * multiplicador1
        multiplicador1 -= 1

    resto1 = (soma1 * 10) % 11
    if resto1 == 10:
        resto1 = 0
        
    if resto1 != cpf_array[9]:
        return False

    # Validação do segundo dígito
    soma2 = 0
    multiplicador2 = 11
    for i in range(10):
        soma2 += cpf_array[i] * multiplicador2
        multiplicador2 -= 1

    resto2 = (soma2 * 10) % 11
    if resto2 == 10:
        resto2 = 0
        
    if resto2 != cpf_array[10]:
        return False

    return True

def validar_nome(nome):

    nome = nome.replace(" ", "")

    return nome.isalpha()

def pedir_coordenada(mensagem):
    while True:
        # Pede o dado e já troca vírgula por ponto (brasileiro adora usar vírgula)
        valor = input(mensagem).strip().replace(",", ".")
        
        try:
            # Tenta converter para float. Se for letra, o Python vai gritar um 'ValueError'
            valor_float = float(valor)
            
            # Se deu certo, retorna o valor convertido em texto para salvar no TXT
            return str(valor_float)
            
        except ValueError:
            # Se deu erro, ele cai aqui e o while True repete a pergunta
            print(" ❌ Erro! A coordenada deve ser um número válido (ex: -8.0475). Tente novamente.")