#Monitorador de vendas do comercio

bananas = int(input("Informe o numero de bananas vendidas:"))
uvas = int(input("Informe o numero de uvas vendidas:"))

if bananas > uvas:
    print ("As bananas tiveram mais vendas!")
elif uvas > bananas:
    print ("As uvas tiveram mais vendas!")
else:
    print("Houve empate nas vendas")
