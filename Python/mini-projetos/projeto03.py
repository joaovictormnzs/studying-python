def valor_gorjeta(a, b):
    return (a*b) / 100

valor_conta = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = valor_gorjeta(valor_conta, porcentagem)

valor_final = valor_conta + gorjeta

print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {valor_final:.2f}")