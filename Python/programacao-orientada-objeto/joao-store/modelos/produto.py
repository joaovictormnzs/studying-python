class Produto: 
    produtos = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() 
        self._categoria = categoria.upper()
        self._ativo = False
        Produto.produtos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}' 
    
    @classmethod
    def listar_produtos(cls):
        print(f'{'Nome do Produto'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for produto in cls.produtos:
            print(f'{produto._nome.ljust(25)} | {produto._categoria.ljust(25)} | {produto.ativo}')
            
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    

computador = Produto('Computador', 'Eletronico')
computador.alternar_estado()
celular = Produto('Celular', 'Eletronico')

Produto.listar_produtos()

