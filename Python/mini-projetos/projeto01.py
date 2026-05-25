def somar(a,b):
    return a + b

try:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))

    resultado = somar(numero1, numero2)
    print(f"A soma dos numeros é: {resultado}")
except ValueError:
    print("Erro: Digite apenas numeros validos!")


