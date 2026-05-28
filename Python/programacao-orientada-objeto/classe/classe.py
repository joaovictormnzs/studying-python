# Uma classe é um molde que define as características (atributos) e os comportamentos (métodos) que um objeto terá. Ela estabelece a estrutura de um tipo de dado, permitindo instanciar múltiplos objetos com propriedades únicas, mas baseados nas mesmas regras.

class produto: # Aqui você está declarando a criação da classe e dando a ela o nome de produto
    nome = '' # Atributo do produto
    categoria = '' # Atributo do produto
    ativo = False # Atributo do produto do tipo Booleano

# Objeto = é a instancia de uma classe

class Musica:
    nome = ''
    artista = ''
    duracao = int

# --- Instanciação de Objetos ---

musica1 = Musica() # --> Objeto 1
musica1.nome = 'Tipo Narutin'
musica1.artista = 'MHRap'
musica1.duracao = 380

musica2 = Musica() # --> Objeto 2
musica2.nome = 'Shape of You'
musica2.artista = 'Ed Sheeran'
musica2.duracao = 234

print(f'Musica: {musica1.artista} - Artista: {musica1.artista} - {musica1.duracao} segundos')