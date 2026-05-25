def caixa_eletronico():
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        valor = int(input("Digite o valor do saque: "))

        if valor <= 0:
            print("Erro: o valor deve ser positivo")
        elif valor % 2 != 0:
            print("Erro: O valor deve ser multiplo de 2")
        else:
            print("Cedulas entregues!")
        
            for cedula in cedulas:
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f"{quantidade} cedulas de R$ {cedula}")
                    valor = valor % cedula
    
    except ValueError:
        print("Erro: Digite um valor numerico valido.")

caixa_eletronico()