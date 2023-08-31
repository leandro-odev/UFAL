'''
#  Função para comprar livro ✅
#  Função para remover Nó ✅
#  Emprestar livro ✅
#? Não lembro mais qual função era pra implementar 😶‍🌫️
'''

from classes.node import Node
from classes.livro import Livro
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def adicionar(self, liv_loc, liv_emp, titulo, autor, edicao, editora, ibms):
        new_node = Node(liv_loc, liv_emp, titulo, autor, edicao, editora, ibms)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
    
    def print_list(self):
        new_node = self.head
        for i in range(self.lenght):
            print(f"Livro número {i+1}")
            print(f"Título: {new_node.value.livro.titulo}")
            print(f"Autor: {new_node.value.livro.autor}")
            print(f"Edição: {new_node.value.livro.edicao}")
            print(f"Editora: {new_node.value.livro.editora}")
            print(f"IBMS: {new_node.value.livro.ibms}")
            print(f"Livros na estante: {new_node.value.livros_local}")
            print(f"Livros emprestados: {new_node.value.livros_emprestado}")
            print("\n")
            new_node = new_node.next

    def find_node_livro(self, livro):
        new_node = self.head
        while new_node:
            if new_node.value.livro.autor == livro.autor and new_node.value.livro.titulo == livro.titulo and new_node.value.livro.edicao == livro.edicao and new_node.value.livro.editora == livro.editora and new_node.value.livro.ibms:
                return new_node
            new_node = new_node.next
        return None

    def comprar(self, livro):
        new_node = self.find_node_livro(livro)
        if new_node:
            new_node.value.livros_local += 1
        else:
            self.adicionar(1, 0, livro.titulo, livro.autor, livro.edicao, livro.editora, livro.ibms)
        
    def remover_no(self, livro):
        if self.lenght == 0:
            return
        new_node = self.head
        new_node2 = None
        while new_node:
            if new_node.value.livro.autor == livro.autor and new_node.value.livro.titulo == livro.titulo and new_node.value.livro.edicao == livro.edicao and new_node.value.livro.editora == livro.editora and new_node.value.livro.ibms:
                new_node2.next = new_node.next
                new_node = None
                self.lenght -= 1
                return
            else:
                new_node2 = new_node
                new_node = new_node.next

    def emprestar(self, livro):
        new_node = self.find_node_livro(livro)
        if not new_node:
            return
        if new_node and new_node.value.livros_local > 0:
            new_node.value.livros_local -= 1
            new_node.value.livros_emprestado += 1
        
        '''
        #* Função para emprestar livro antes
        new_node = self.head
        for i in range(self.lenght):
            if new_node.value.livro.autor == livro.autor and new_node.value.livro.titulo == livro.titulo and new_node.value.livro.edicao == livro.edicao and new_node.value.livro.editora == livro.editora and new_node.value.livro.ibms == livro.ibms:
                if new_node.value.livros_local > 0:
                    new_node.value.livros_local -= 1
                    new_node.value.livros_emprestado += 1
                    return
                else:
                    return
            new_node = new_node.next
        '''

my_linked_list = LinkedList()
my_linked_list.adicionar(3, 2, 'Clube de Regatas Vasco da Gama', 'Vasco da Gama', 1898, 'Leandro', 1000)
my_linked_list.adicionar(7, 0, 'Livro 2', 'Sla 2', 2000, 'Nome 2', 600)
my_linked_list.adicionar(2, 1, 'Livro 3', 'Sla 3', 2500, 'Nome 3', 700)

x = Livro('Livro 2', 'Sla 2', 2000, 'Nome 2', 600)

my_linked_list.emprestar(x)

my_linked_list.print_list()
