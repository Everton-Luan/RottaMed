def exibir_boas_vindas():
    print("Olá! Sou o Rottinha.")
    print("Vou te fazer algumas perguntas simples para")
    print("indicar a melhor unidade para o seu caso.")
    print("-" * 45)

def perguntar_gravidade():
    print("\nComo você descreveria o que está sentindo agora?")
    print("[1] - Sintomas graves e repentinos (Ex: dor no peito, falta de ar forte, suspeita de fratura, cortes profundos, febre muito alta).")
    print("[2] - Sintomas leves ou rotina (Ex: dor de cabeça leve, vacinação, renovar receita, sintomas de gripe leve, check-up).")
    print("[3] - Sair do assistente")
    
    opcao = input("▶ Escolha uma opção: ").strip()
    while opcao not in ["1", "2", "3"]:
        opcao = input("Opção inválida!! Digite 1, 2 ou 3: ").strip()
    
    return opcao

def exibir_resultado(tipo_unidade):
    print("\n" + "=" * 45)
    print(" RESULTADO DA TRIAGEM ".center(45))
    print("=" * 45)
    
    if tipo_unidade == "UPA":
        print("ATENÇÃO: Seus sintomas indicam necessidade de atendimento imediato")
        print("Recomendação: Procure a UPA mais próxima!")
    
    elif tipo_unidade == "UBS":
        print("Seus sintomas parecem ser leves ou de rotina.")
        print("Recomendação: Procure uma UBS (Posto de Saúde).")
        
    print("=" * 45)