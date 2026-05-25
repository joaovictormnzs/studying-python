def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError # Tratamento de erro para divisores por zero
    return num1 / num2

def calculadora():

    try:
        num1 = float(input("Digite o primeiro numero: "))
        operacao = input("Selecione o operador: + | - | * | / : ")
        num2 = float(input("Digite o segundo numero: "))

        if operacao == "+":
            resultado = somar(num1, num2) # variavel resultado criada dentro do laço if
        elif operacao == "-":
            resultado = subtrair(num1, num2)
        elif operacao == "*":
            resultado = multiplicar(num1, num2)
        elif operacao == "/":
            resultado = dividir(num1, num2)
        else:
            print("Selecione um operador valido!")
            return
        
        print(f"Resultado: {resultado}")
    
    except ValueError: # Tratamento de erros
        print("Erro: Entrada invalida. Digite apenas numeros.")
    except ZeroDivisionError:
        print("Erro: Divisao por zero nao é permitida.")

calculadora() 