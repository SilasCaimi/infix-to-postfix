from Node import *

class Pilha():
    def __init__(self):
        self.topo = None
        self.cont = 0

    def __str__(self):
        strPilha = ""
        node = self.topo
        while True:
            strPilha += str(node.valor) + "\n"
            node = node.prox
            if node == None:
                break
        return strPilha

    def isEmpty(self):
        if self.topo == None:
            return True
        else:
            return False

    def push(self, v):
        if self.isEmpty():
            self.topo = Node(v)
            self.cont += 1
        else:
            novo = Node(v, self.topo)
            self.topo = novo
            self.cont += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Pilha vazia")
        v = self.topo.valor
        self.topo = self.topo.prox
        self.cont -= 1
        return v

    def stacktop(self):
        if self.isEmpty():
            raise Exception("Pilha vazia")
        return self.topo.valor 