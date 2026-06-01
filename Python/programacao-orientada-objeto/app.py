from modelos.produto import Produto

teclado_magnetico = Produto('Teclado Magnetico', 'Eletronico')
teclado_magnetico.receber_avaliacao('Joao', 10)
teclado_magnetico.receber_avaliacao('Iza', 5)





def main():
    Produto.listar_produtos()

if __name__ == '__main__':
    main()