texto = input("Digite um texto: ")

palavras_grandes = [] # Lista vazia

for palavra in texto.split():
    if len(palavra) > 10:
        palavras_grandes.append(palavra) # Se uma palavra tiver mais de 10 caracteres adiciona na lista vazia

if palavras_grandes:
    print("Palavras longas encontradas:")
    for palavra in palavras_grandes:
        print(palavra)
else:
    print("Nenhuma palavra grande encontrada.")
