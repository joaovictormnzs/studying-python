
# Definindo a classe Carro para criar objetos do tipo Carro.
class Carro:
    carros = [] # Será armazenado nessa lista todas as instâncias (objeto) que criamos.

    # Método Construtor (__init__): É chamado automaticamente sempre que criamos um novo carro.
    # O parâmetro 'self' representa o objeto específico que está sendo criado naquele momento.
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo #Atributo de instância
        self.cor = cor #Atributo de instância
        self.ano = ano #Atributo de instância
        Carro.carros.append(self) # Acessamos a lista da classe (Carro.carros) e adicionamos o carro que acabou de ser criando (self) dentro dela. 
    
    def __str__(self): # Método Especial (__str__): Define como o objeto deve ser representado em texto.
    # É ativado automaticamente quando você tenta dar um 'print(objeto)'
        return f'{self.modelo} | {self.cor} | {self.ano}'
    

    def listar_carros(): # Criando Método de Classe: Não recebe o 'self' porque o objetivo dele não é olhar para um carro individual, mas sim operar sobre a lista geral da classe.
        for carro in Carro.carros: # Percorre cada objeto 'carro' guardado dentro da lista da classe
            print(f'Modelo: {carro.modelo} | Cor: {carro.cor} | Ano: {carro.ano}') # Acessa os atributos de instância de cada um dos carros e exibe no terminal

# --- Instanciação de Objetos ---

carro_joao = Carro(modelo='Civic G9', cor='Preto Fosco', ano=2012) # Criando o primeiro objeto passando os argumentos de forma nomeada
carro_isa = Carro('Jeep', 'Preto', 2020) # Criando o segundo objeto passando os argumentos de forma posicional

print(carro_joao) # Aparece os atributos por conta do metodo (__str__). Sem ele aparecia um codigo de memoria estranho no terminal
print(carro_isa)

Carro.listar_carros() # Chamamos o método diretamente a partir da classe 'Carro' para listar todos os carros criados.