def contar_vogais(texto):
    vogais = "aeiou"
    quantidade = 0

    for letra in texto.lower(): # Um laço que passa por cada caractere do texto, um por um.
        if letra in vogais: # Verifica se a letra da vez está dentro da sua string/lista de vogais.
            quantidade +=1 # Se a letra for uma vogal, ele soma 1 ao contador.
        
    return quantidade

texto = input("Digite a frase: ")
print(f"O texto possui {contar_vogais(texto)} vogais")