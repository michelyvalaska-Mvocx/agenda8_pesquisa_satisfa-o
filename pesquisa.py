contador_excelente = 0
contador_ruim = 0
total_entrevistados = 10

print(f"--- PESQUISA DE OPINIAO - {total_entrevistados} ENTREVISTADOS ---")

for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado {i}/{total_entrevistados}")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    print("Opiniao sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = input("Digite a opiniao (1, 2 ou 3): ")

    if opiniao == "1":
        contador_excelente = contador_excelente + 1
    elif opiniao == "3":
        contador_ruim = contador_ruim + 1
    elif opiniao == "2":
        pass
    else:
        print("Opcao invalida considerada como nao contabilizada")

print("\n--- RESULTADO FINAL DA PESQUISA ---")
print(f"a) Quantidade de respostas 'EXCELENTE': {contador_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {contador_ruim}")


