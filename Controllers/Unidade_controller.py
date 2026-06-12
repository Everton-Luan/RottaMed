import Models.Unidade_model as model
import Views.Unidade_view as view

ARQUIVO =  "database/unidades.txt"


#Criando unidade
def iniciar_cadastro_unidade():
    #Chama a View para pegar os dados da nova unidade 
    nome, tipo, fluxo, espec, cpf, senha, latitude, longitude = view.add_dados_unidade()

    unidades_existentes = model.ler_dados_txt()
    for u in unidades_existentes:
        if u["nome"].upper() == nome.upper():
            view.menssagem(f"\n Erro: Já existe uma unidade cadastrada com o nome '{nome}'.")
            return # Cancela o cadastro imediatamente e volta para o menu
    
    #Estrutura os dados recebidos em um dicionario usando o model s
    nova_unidade = model.criar_dicionario_unidade(nome, tipo, fluxo, espec, cpf, senha, latitude, longitude)
    
    # Salva
    model.salvar_unidade(nova_unidade)
    view.menssagem(" Unidade cadastrada com sucesso!!")

# Parte do Read

#Lê e mostra todas as unidades
def iniciar_busca_geral():
    todas_as_unidades = model.ler_dados_txt()
    
    # Manda a View mostrar a lista inteira
    view.exibir_unidades(todas_as_unidades)


#Lê e mostra uma unidade
def iniciar_busca_especifica():
    unidade_procurada = view.pedir_nome_busca().upper()
    
    #Pega todas as unidades do TXT
    todas_as_unidades = model.ler_dados_txt()
    
    #Procura e se achar o nome, guarda a unidade e para de procurar
    unidade_encontrada = None
    for u in todas_as_unidades:
        if u["nome"].upper() == unidade_procurada:
            unidade_encontrada = u
            break 
            
    #Manda a View mostrar o resultado (pode ser a unidade ou um aviso de erro)
    view.exibir_unidade_unica(unidade_encontrada)

#Parte do Update

#Atualiza os dados de uma unidade
def iniciar_atualizacao():
    #Pede para a View o nome da unidade que será editada
    view.menssagem("\n" + "="*45)
    view.menssagem(" ATUALIZAR UNIDADE ".center(45))
    view.menssagem("="*45)

    unidade_procurada = view.pedir_nome_busca().upper()
    
    #Puxa as unidades do banco de dados
    lista_unidades = model.ler_dados_txt() 
    
    #Variáveis para rastrear se achamos a unidade
    indice_encontrado = -1
    
    #Procura a unidade na lista
    for i, u in enumerate(lista_unidades):
        if u["nome"].upper() == unidade_procurada:
            indice_encontrado = i # Guarda a posição (índice) dela na lista
            break # Achou, pode parar de procurar
            
    #S o index continuar -1, é porque o for acabou e não achou nada
    if indice_encontrado == -1:
        view.menssagem("\n Unidade não encontrada para atualização.")
        return
        
    #Mostra a unidade atual para o usuário ver o que vai mudar
    print("\n[Dados Atuais da Unidade]:")
    view.exibir_unidade_unica(lista_unidades[indice_encontrado])
    
    #Chama a função da view e valida os dados
    view.menssagem("\n[Digite os Novos Dados]:")
    nome, tipo, fluxo, espec, cpf, senha, latitude, longitude = view.add_dados_unidade()
    
    #Atualiza o dicionário na lista
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
    
    #O Model salva essa lista atualizada 
    model.modificar_unidades(lista_unidades)
    
   
    view.menssagem("\n Unidade atualizada com sucesso no sistema!")

def iniciar_exclusao():
    print("\n===== EXCLUIR UNIDADE =====")

    #Pede o nome e puxa a lista completa
    unidade_procurada = view.pedir_nome_busca().upper()
    lista_unidades = model.ler_dados_txt() 
    indice_encontrado = -1

    #Busca a unidade na lista
    for i, u in enumerate(lista_unidades):
        if u["nome"].upper() == unidade_procurada:
            indice_encontrado = i 
            break

    #Se não achou, encerra
    if indice_encontrado == -1:
        print("\n Unidade não encontrada para exclusão.")
        return
    
    #Mostra a unidade para o usuário saber o que está prestes a apagar
    print("\n[Dados da Unidade a ser excluída]:")
    view.exibir_unidade_unica(lista_unidades[indice_encontrado])

    #Pede a confirmação final
    if view.confirmacao_exclusao():
        
        #O comando .pop() vai na lista e tira o que tem naquela posição
        lista_unidades.pop(indice_encontrado)

        #O model reescreve a lista
        model.modificar_unidades(lista_unidades)


        view.menssagem("\n Unidade excluída com sucesso do sistema!")
    else:
        view.menssagem("\n Exclusão cancelada. A unidade foi mantida no sistema.")
  