import os

produtos = [{'nome':'Celular', 'categoria':'Eletronico', 'ativo':False},
           {'nome':'Computador', 'categoria':'Eletronico', 'ativo':True}]

def exibir_nome_do_programa():
    ''' Essa função retorna o titulo do programa'''
    print("""
░░█ █▀█ ▄▀█ █▀█   █▀ ▀█▀ █▀█ █▀█ █▀▀
█▄█ █▄█ █▀█ █▄█   ▄█ ░█░ █▄█ █▀▄ ██▄
""")

def exibir_opcoes():
    ''' Essa função retorna a lista de opções do sistema'''
    print('1. Cadastrar produto')
    print('2. Listar produtos')
    print('3. Alternar estados dos produtos')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função finaliza o sistema'''
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    '''Essa função é utilizada quando houver uma opção ínvalida no sistema'''
    print('Opção Inválida!')
    voltar_ao_menu_principal()

def cadastrar_novo_produto():
    '''Essa função serve para cadastar um novo produto'''
    exibir_subtitulo('Cadastrar Novo Produto')

    nome_produtos = input('Digite o nome do produto: ')
    categoria = input(f'Digite o nome da categoria do produto {nome_produtos}: ')
    dados_do_produto = {'nome': nome_produtos, 'categoria': categoria, 'ativo':False}
    produtos.append(dados_do_produto)
    print(f'O produto {nome_produtos} foi cadastrado com sucesso!') 

    voltar_ao_menu_principal()

def listar_produtos():
    '''Essa função serve para listar todos os produtos cadastrados'''
    exibir_subtitulo('Lista de Produtos')

    print(f'{'Nome do Produto'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for produto in produtos:
        nome_produtos = produto['nome'] 
        categoria = produto['categoria']
        ativo = 'Ativado' if produto['ativo'] else 'Desativado'
        print(f'{nome_produtos.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar para o menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Essa função serve para exibir o subtitulo de cada opção selecionada'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def alternar_estado_produto():
    '''Essa função serve para alternar o estado do produto (Ativado/Desativado)'''
    exibir_subtitulo('Alternarando estado do produto')

    nome_produto = input('Digite o nome do produto que deseja alterar o estado: ')
    produto_encontrado = False

    for produto in produtos:
        if nome_produto == produto['nome']:
            produto_encontrado = True
            produto['ativo'] = not produto['ativo'] 
            mensagem = f'O produto {nome_produto} foi ativado com sucesso!' if produto['ativo'] else f'O produto {nome_produto} foi desativado com sucesso!'
            print(mensagem)
    if not produto_encontrado:
        print('O produto nao foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) # input recebendo o valor como numero inteiro

        if opcao_escolhida == 1: 
            cadastrar_novo_produto()
        elif opcao_escolhida == 2:
            listar_produtos()
        elif opcao_escolhida == 3:
            alternar_estado_produto()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função retorna a interface inicial do programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()