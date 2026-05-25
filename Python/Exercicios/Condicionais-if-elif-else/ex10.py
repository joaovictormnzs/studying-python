# Aprovando empréstimo

renda = float(input("Digite a sua renda mensal: "))
parcela = float(input("Digite a parcela desejada: "))

if (renda > 2000 and parcela <= 0.3 * renda):
    print("Emprestimo aprovado!")
elif renda <= 2000:
    print("Emprestimo negado: Renda mensal abaixo do minimo")
else:
    print("Emprestimo negado: parcela acima de 30% da renda.")
