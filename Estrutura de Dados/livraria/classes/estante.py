from classes.livro import Livro

class Estante:
    def __init__(self, liv_loc, liv_emp, titulo, autor, edicao, editora, ibms):
        self.livro = Livro(titulo, autor, edicao, editora, ibms)
        self.livros_local = liv_loc
        self.livros_emprestado = liv_emp