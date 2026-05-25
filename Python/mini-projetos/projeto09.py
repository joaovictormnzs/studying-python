import random

def adivinhar_numero(): # funcao para sortear um numero entre 1 e 100
    numero_secreto = random.randint(1,100)
    tentativas = 0 # contador de tentivas

    while True:
        try: 
            palpite = int(input("Escolha um numero entre 1 e 100: "))

            if not 1 <= palpite <= 100: # se for um numero invalido, continua a execuçao 
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
            
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente")
            else:
                print(f"Parabens! Voce acertou o {numero_secreto} em {tentativas} tentativas.")
                break
        
        except ValueError as erro:
            print(f"Entrada inválida: {erro}")

adivinhar_numero()



