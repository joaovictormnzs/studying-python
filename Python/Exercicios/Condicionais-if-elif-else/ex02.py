# Calculando o tempo total de projeto

A = int(input("Informe os dias para a atividade A: "))
B = int(input("Informe os dias para a atividade B: "))
C = int(input("Informe os dias para a atividade C: "))

if (A >= 0 and B >= 0 and C >= 0 ):
    somaTotal = A + B + C
    print(f"O tempo total do projeto e de {somaTotal} dias")
else:
    print("Os dias nao podem ser negativos!")

