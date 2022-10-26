class Pessoa:
    numero_olhos = 2

    def __init__(self, *filhos, nome = None, idade=59) -> None:
        self.nome = nome
        self.idade =idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, sou  {self.nome}'
    
    @staticmethod
    def metodo_estatico():
        return 32
    
    @classmethod
    def metodo_atributo_classe(cls):
        return f'Classe = {cls} número de olhos = {cls.numero_olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    numero_olhos = 4

    def cumprimentar(self):
        cumprimentar_class_pai = super().cumprimentar()
        return f'{cumprimentar_class_pai}. Sou um mutante.'
    

if __name__ == '__main__':
    paulo = Mutante('Isadora', nome='Paulo')
    isabel = Pessoa(nome='Isabel', idade=63)
    francisco = Pessoa(isabel,paulo, nome='Francisco', idade=89)
    print(paulo.nome)
    print(francisco.nome)
    for filho in francisco.filhos:
        print(filho.nome)
    print(paulo.__dict__)
    print(Pessoa.metodo_estatico(), paulo.metodo_estatico())
    print(Pessoa.metodo_atributo_classe(), paulo.metodo_atributo_classe())
    print(isinstance(paulo, Pessoa))
    print(isinstance(paulo, Homem))
    print(f'Número de olhos: {paulo.numero_olhos}')
    print(isabel.cumprimentar())
    print(paulo.cumprimentar())