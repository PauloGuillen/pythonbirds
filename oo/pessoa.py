class Pessoa:
    numero_olhos = 2

    def __init__(self, *filhos, nome = None, idade=59) -> None:
        self.nome = nome
        self.idade =idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        print(f'Olá {id(self)}')

if __name__ == '__main__':
    paulo = Pessoa('Isadora', nome='Paulo')
    isabel = Pessoa(nome='Isabel', idade=63)
    francisco = Pessoa(isabel,paulo, nome='Francisco', idade=89)
    print(paulo.nome)
    print(francisco.nome)
    for filho in francisco.filhos:
        print(filho.nome)
    paulo.sobrenome = 'Guillén'
    print(francisco.__dict__)
    print(isabel.__dict__)
    print(paulo.__dict__)
    Pessoa.numero_olhos = 3
    print(Pessoa.numero_olhos)
    print(paulo.numero_olhos)
    print(id(Pessoa.numero_olhos), id(paulo.numero_olhos), id(francisco.numero_olhos))
    paulo.numero_olhos = 1
    print(paulo.numero_olhos)
    print(id(Pessoa.numero_olhos), id(paulo.numero_olhos), id(francisco.numero_olhos))
    print(paulo.__dict__)