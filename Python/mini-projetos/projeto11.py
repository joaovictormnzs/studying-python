def gerenciador_de_tarefas():
    tarefas = []

    while True:
        print("Gerenciador de tarefas\n")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefas")
        print("4. Sair\n")

        opcao = input("Selecione uma das opcoes: ")

        if opcao == "1": 
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa: # verifica se a lista está vazia
                tarefas.append(tarefa) # adiciona a tarefa na lista vazia tarefas
                print("Tarefa adicionada!")
            else:
                print("O campo de tarefa nao pode ficar vazia.")
        
        elif opcao == "2":
            if tarefas:
                print("\nTarefas")
                for i, tarefa in enumerate(tarefas, 1): # python lê da direita para esquerda. o 1 significa por onde deve começar a contar. 
                    print(f"{i}. {tarefa}")
            else: 
                print("Nenhuma tarefa encontrada.")
        
        elif opcao == "3":
            if not tarefas: # verifica se a lista está vazia, se estiver volta para o menu principal
                print("Nenhuma tarefa para remover.") 
                continue

            try: 
                indice = int(input("Digite o numero da tarefa para ser removida: ")) # nas listas o indice começa do zero = 2 tarefas ( indices 0, 1 )
                if 0 <= indice < len(tarefas): # checa de o numero é maior ou igual a zero e menor que o numero de tarefas adicionadas
                    removida = tarefas.pop(indice) # remoçao da tarefa da lista
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Erro: Indice Invalido! Digite um numero valido!")
            except ValueError:
                print("Erro: entrada invalida! Digite um numero.")
        
        elif opcao == "4":
            print("Saindo do gerenciador de tarefas.") 
            break

        else:
            print("Digite uma opcao valida! Escolha um numero entre 1 e 4.")

gerenciador_de_tarefas()