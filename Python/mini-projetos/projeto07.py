import random

def gerar_senha():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"

    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiais)
    ]

    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8)) # k é a variavel que a funcao random_choices espera receber para inicializar
    random.shuffle(senha) # garante aleatoriedade em todos os caracteres
    return ''.join(senha) # converter a lista em string

print(f"Senha gerada: {gerar_senha()}")