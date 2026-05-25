# Calculando pedágio

distancia = int(input("Informe o valor da distancia percorrida (km): "))

if distancia <= 100:
    print("Valor do pedagio: R$ 10,00")
elif distancia <= 200:
    print("Valor do pedagio: R$ 20,00")
else:
    print ("Valor do pedagio: R$ 30,00")