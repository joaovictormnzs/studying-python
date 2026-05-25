def validar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas numeros"
    if len(cpf) != 11:
        return "Erro: o CPF deve conter apenas 11 numeros"
    return "CPF válido"

cpf = input("Digite o seu CPF: ")
print(validar_cpf(cpf))


