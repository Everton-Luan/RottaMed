# Importe os arquivos necessários dependendo de onde colocar esta função
from Models import Unidade_model
from Views import Unidade_view

def iniciar_atualizacao_gestor():
    print("\n===== ATUALIZAR UNIDADE (GESTOR) =====")
    
    # 1. Pede o nome para buscar (reutilizando a função que você já tem)
    unidade_procurada = Unidade_view.pedir_nome_busca().upper()
    
    # 2. Puxa a lista completa e procura
    lista_unidades = Unidade_model.ler_dados_txt() # Use a sua função de leitura aqui
    indice_encontrado = -1
    
    for i, u in enumerate(lista_unidades):
        if u["nome"].upper() == unidade_procurada:
            indice_encontrado = i 
            break 
            
    # 3. Se não achou, encerra
    if indice_encontrado == -1:
        print("\n❌ Unidade não encontrada.")
        return 
        
    # 4. Separa a unidade encontrada em uma variável para ficar mais fácil de ler
    unidade = lista_unidades[indice_encontrado]
    
    # 5. Manda a unidade para a View perguntar os novos dados
    novo_fluxo, nova_espec = Unidade_view.gestor_atualiza_dados(unidade)

    # Nós NÃO mexemos no nome, tipo, CPF ou senha. Só substituímos estas duas chaves!
    unidade["fluxo"] = novo_fluxo
    unidade["especializações"] = nova_espec
    
    # Devolvemos a unidade alterada para a lista
    lista_unidades[indice_encontrado] = unidade
    
    # 6. Manda o Model salvar a lista inteira por cima do arquivo velho
    Unidade_model.modificar_unidades(lista_unidades)
    
    print("\n✅ Fluxo e Especializações atualizados com sucesso!")