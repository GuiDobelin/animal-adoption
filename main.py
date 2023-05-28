class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
class Fila:
    def __init__(self):
        self.items = []

    def vazia(self):
        return len(self.items) == 0
    
    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if self.vazia():
            return None
        return self.items.pop(0)
    
    def tamanho(self):
        return len(self.items)

class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return len(self.items) == 0

    def Salva(self, item):
        self.items.append(item)