class Produto: 
    produtos = []

    def __init__(self, nome, categoria):
        self.nome = nome 
        self.categoria = categoria 
        self.ativo = False
        Produto.produtos.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}' 
    
    def listar_produtos():
        for produto in Produto.produtos:
            print(f'Produto: {produto.nome} | Categoria: {produto.categoria} | Ativo: {produto.ativo}')

computador = Produto('Computador', 'Eletronico')
celular = Produto('Celular', 'Eletronico')

Produto.listar_produtos()

