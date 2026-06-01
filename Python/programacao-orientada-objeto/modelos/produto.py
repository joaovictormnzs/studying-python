from modelos.avaliacao import Avaliacao

class Produto: 
    produtos = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de um produto.

        Parâmetros:
        - nome (str): O nome do produto.
        - categoria (str): A categoria do produto.
        """
        self._nome = nome.title() 
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Produto.produtos.append(self)

    def __str__(self):
        """ Retorna uma apresentacao em string do produto"""
        return f'{self._nome} | {self._categoria}' 
    
    @classmethod
    def listar_produtos(cls):
        """retorna uma lista formatada dos produtos cadastrados"""
        print(f'{'Nome do Produto'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'}')
        for produto in cls.produtos:
            print(f'{produto._nome.ljust(25)} | {produto._categoria.ljust(25)} | {str(produto.media_avaliacoes).ljust(25)} | {produto.ativo}')
            
    @property
    def ativo(self):
        """Retorna o estado de atividade do produto"""
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado(self):
        """Alterna o estado da atividade do produto """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o produto.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a produto.
        - nota (float): A nota atribuída ao produto (entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do produto."""
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_de_notas, 1)
        return media