# Controlando o orçamento mensal

limite = 3000.0 
despesas = float(input("Digite o total de despesas: R$ "))

if despesas > limite:
    print("Alerta! Voce ultrapassou o limite de orcamento.")
else:
    print("Voce esta dentro do orcamento.")