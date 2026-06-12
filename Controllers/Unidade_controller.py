import Models.Unidade_model as model
import Views.Unidade_view as view

ARQUIVO =  "database/unidades.txt"

# Parte do Create

# Criando unidade
def iniciar_cadastro_unidade():
    # Chama a View para pegar os dados da nova unidade 
    nome, tipo, fluxo, espec, cpf, senha, latitude, longitude = view.add_dados_unidade()

    unidades_existentes = model.ler_dados_txt()
    for u in unidades_existentes:
        if u["nome"].upper() == nome.upper():
            view.menssagem(f"\n ❌ Erro: Já existe uma unidade cadastrada com o nome '{nome}'.")
            return # Cancela o cadastro imediatamente e volta para o menu
    
    # Estrutura os dados recebidos em um dicionario usando o model para serem padronizados
    nova_unidade = model.criar_dicionario_unidade(nome, tipo, fluxo, espec, cpf, senha, latitude, longitude)
    
    # Salva
    model.salvar_unidade(nova_unidade)
    view.menssagem(" ✅ Unidade cadastrada com sucesso!!")

# Parte do Read

# 1. Lê e imprime TODAS as unidades
def iniciar_busca_geral():
    # Pega todas as unidades cadastradas
    todas_as_unidades = model.ler_dados_txt()
    
    # Manda a View mostrar a lista inteira
    view.exibir_unidades(todas_as_unidades)


# 2. Lê e imprime uma UNICA unidade
def iniciar_busca_especifica():
    # Pede para a View perguntar o nome
    unidade_procurada = view.pedir_nome_busca().upper()
    
    # Pega todas as unidades do TXT
    todas_as_unidades = model.ler_dados_txt()
    
    # Faz uma busca: se achar o nome, guarda a unidade e para de procurar
    unidade_encontrada = None
    for u in todas_as_unidades:
        if u["nome"].upper() == unidade_procurada:
            unidade_encontrada = u
            break 
            
    # Manda a View mostrar o resultado (pode ser a unidade ou um aviso de erro)
    view.exibir_unidade_unica(unidade_encontrada)

# Parte do Update

# Atualiza os dados de uma UNICA unidade
def iniciar_atualizacao():
    # 1. Pede para a View o nome da unidade que será editada
    view.menssagem("\n" + "="*45)
    view.menssagem(" ATUALIZAR UNIDADE ".center(45))
    view.menssagem("="*45)

    unidade_procurada = view.pedir_nome_busca().upper()
    
    # 2. Puxa TODAS as unidades do banco de dados (usando sua função de leitura)
    lista_unidades = model.ler_dados_txt() 
    
    # 3. Variáveis para rastrear se achamos a unidade
    indice_encontrado = -1
    
    # 4. Procura a unidade na lista
    for i, u in enumerate(lista_unidades):
        if u["nome"].upper() == unidade_procurada:
            indice_encontrado = i # Guarda a posição (índice) dela na lista
            break # Achou, pode parar de procurar
            
    # 5. Se o index continuar -1, é porque o for acabou e não achou nada
    if indice_encontrado == -1:
        view.menssagem("\n ❌ Unidade não encontrada para atualização.")
        return
        
    # 6. Mostra a unidade atual para o usuário ver o que vai mudar
    print("\n[Dados Atuais da Unidade]:")
    view.exibir_unidade_unica(lista_unidades[indice_encontrado])
    
    # 7. Chama a sua função incrível da View que pede os dados e valida tudo
    view.menssagem("\n[Digite os Novos Dados]:")
    nome, tipo, fluxo, espec, cpf, senha, latitude, longitude = view.add_dados_unidade()
    
    # 8. Atualiza o dicionário NA LISTA (substitui o antigo pelo novo)
    lista_unidades[indice_encontrado] = {
        "nome": nome,
        "tipo": tipo,
        "fluxo": fluxo,
        "especializações": espec,
        "cpf_gestor": cpf,
        "senha_gestor": senha,
        "latitude": latitude,
        "longitude": longitude
    }
    
    # 9. Manda o Model salvar essa lista atualizada por cima do arquivo velho
    model.modificar_unidades(lista_unidades)
    
    # 10. Avisa que deu tudo certo
    view.menssagem("\n ✅ Unidade atualizada com sucesso no sistema!")

def iniciar_exclusão():
    print("\n===== EXCLUIR UNIDADE =====")

    # Pede o nome e puxa a lista completa
    unidade_procurada = view.pedir_nome_busca().upper()
    lista_unidades = model.ler_dados_txt() 
    indice_encontrado = -1

    # Caça a unidade na lista
    for i, u in enumerate(lista_unidades):
        if u["nome"].upper() == unidade_procurada:
            indice_encontrado = i 
            break

    # Se não achou, encerra
    if indice_encontrado == -1:
        print("\n ❌ Unidade não encontrada para exclusão.")
        return
    
    # Mostra a unidade para o usuário saber o que está prestes a apagar
    print("\n[Dados da Unidade a ser excluída]:")
    view.exibir_unidade_unica(lista_unidades[indice_encontrado])

    # Pede a confirmação final
    if view.confirmacao_exclusao():
        
        # O comando .pop() vai na lista e arranca fora o item daquela posição
        lista_unidades.pop(indice_encontrado)

        # Manda o Model reescrever o arquivo com essa lista (agora com um item a menos)
        model.modificar_unidades(lista_unidades)

        # Mensagem de sucesso
        view.menssagem("\n 🗑️ Unidade excluída com sucesso do sistema!")
    else:
        view.menssagem("\n ❌ Exclusão cancelada. A unidade foi mantida no sistema.")
  