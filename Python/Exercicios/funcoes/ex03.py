def saudacao(hora):
    if hora < 12:
        return "Bom dia!"
    elif hora >= 12 and hora <= 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

hora_atual = int(input("Digite a hora atual: "))
print(saudacao(hora_atual))