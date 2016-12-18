class jogador:
    def __init__(self, nome, time, n):
        self.nome = nome
        self.time = time
        self.n = n
        self._t = (self.nome, self.time, self.n)

    def __repr__(self):
        return 'Jogador(nome={}, time={}, n={})'.format(self.nome,
                                                        self.time,
                                                        self.n)

    def __getitem__(self, n):
        return self._t[n]

    def __len__(self):
        return len(self._j)

    def count(self, att):
        return len([x for x in self._t if x == att])

    def index(self, att):
        for x, y in enumerate(self._t):
            if y == att:
                return x
