class Pessoa:
    def __init__(self, *filhos, nome = None, idade=59) -> None:
        self.nome = nome
        self.idade =idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        print(f'Olá {id(self)}')

if __name__ == '__main__':
    paulo = Pessoa(nome='Paulo')
    isabel = Pessoa(nome='Isabel')
    francisco = Pessoa(isabel,paulo, nome='Francisco')
    print(paulo.nome)
    print(francisco.nome)
    for filho in francisco.filhos:
        print(filho.nome)

