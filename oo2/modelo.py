class Programa:
    def __init__(self, nome, ano):
        self._nome  = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    #essa é uma função interna do python responsavel pela representação textual da classe
    def __str__(self):
        return f' {self._nome} - {self.ano} : {self._likes} : Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # essa é uma função interna do python responsavel pela representação textual da classe
    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.duracao} min - {self._likes} : Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # essa é uma função interna do python responsavel pela representação textual da classe
    def __str__(self):
        return  f' {self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} : Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - gerra infinita', 2019, 160)
atlanta = Serie("atlanta", 2018, 4)
tmep = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 3)


vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    #Nesse ponto ocorre o polimorfismo, o print vai ocorrer independentemente da classe filha
    print(programa)