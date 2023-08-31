from classes.estante import Estante

class Node:
    def __init__(self, liv_loc, liv_emp, titulo, autor, edicao, editora, ibms):
        self.value = Estante(liv_loc, liv_emp, titulo, autor, edicao, editora, ibms)
        self.next = None