# Calculando IMC

peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite seu altura (m): "))

imc = peso / (altura**2)

print(f"Seu IMC e de: {imc:.2f}")

if imc < 18.5:
    print(" voce esta abaixo do peso")
elif imc < 25:
    print("voce esta com peso normal")
else: 
    print("Voce esta acima do peso")