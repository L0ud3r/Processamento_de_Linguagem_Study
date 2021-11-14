class Triangle:

    # Constructor
    def __init__(self, height, base):
        self.height = height
        self.base = base

    # OU
    #
    # def __init__(self, height=0, base=0):
    #     self.height = height
    #     self.base = base

    # ???
    def __str__(self):
        return f"Triangle of size: heigth={self.height}, base={self.base}"

    # Representa toda a informaçao sobre um objeto
    def __repr__(self):
        return f"Triangle of size: heigth={self.height}, base={self.base}"

    # Funcao que altera os tamanhos do triangulo (a nível de escala)
    def change_size_mult(self, ammount):
        self.height *= ammount
        self.base *= ammount

    # Funcao que calcula área do triangulo
    def area(self):
        return (self.base * self.height) / 2
