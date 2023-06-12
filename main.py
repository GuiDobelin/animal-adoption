from animal import *
from pessoa import *


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

    def empurra(self, item):
        self.items.append(item)

    def pop(self):
        if self.vazia():
            return None
        return self.items.pop()

    def tamanho(self):
        return len(self.items)

def cadastrar_animal():
    tipo = input("Tipo do animal: ")
    while True:
        idade = input("Idade aproximada do animal: ")
        if idade.isdigit():
            idade = int(idade)
            break 
        else:
            print("Idade inválida. Por favor, digite apenas números.")
    cor = input("Cor do animal: ")
    porte = input("Porte do animal: ")
    particularidade = input("Particularidade do animal: ")

    animal = Animal(tipo, idade, cor, porte, particularidade)
    animais_cadastrados.enfileirar(animal)
    print("Animal cadastrado com sucesso!")

def cadastrar_pessoa():
    nome = input("Nome da pessoa: ")
    while True:
        telefone = input("Telefone da pessoa: ")
        if telefone.isdigit():
            telefone = int(telefone)
            break 
        else:
            print("Idade inválida. Por favor, digite apenas números.")
    especie_interesse = input("Espécie de interesse para adoção: ")
    preferencia_animal = input("Preferência de animal: ")

    pessoa = Pessoa(nome, telefone, especie_interesse, preferencia_animal)
    pessoas_interessadas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def gerar_relatorio():
    especie = input("Espécie de animal: ")
    candidatos = []
    current = pessoas_interessadas.head
    while current:
        if current.data.especie_interesse == especie:
            candidatos.append(current.data)
        current = current.next

    if candidatos:
        print("Candidatos para adoção da espécie", especie)
        for candidato in candidatos:
            print("Nome:", candidato.nome)
            print("Telefone:", candidato.telefone)
            print("Preferência de animal:", candidato.preferencia_animal)
            print()
    else:
        print("Nenhum candidato encontrado para adoção da espécie", especie)



def pesquisar_animal():
    caracteristicas = input("Características do animal: ")

    animais_encontrados = []
    for animal in animais_cadastrados.items:
        if caracteristicas.lower() in animal.tipo.lower():
            animais_encontrados.append(animal)

    if animais_encontrados:
        print("Animais encontrados:")
        for animal in animais_encontrados:
            print("Tipo:", animal.tipo)
            print("Idade:", animal.idade)
            print("Cor:", animal.cor)
            print("Porte:", animal.porte)
            print("Particularidade:", animal.particularidade)
            print()
    else:
        print("Nenhum animal encontrado com as características informadas.")

def exibir_menu():
    print("1. Cadastrar animal")
    print("2. Cadastrar pessoa interessada")
    print("3. Gerar relatório de candidatos para adoção")
    print("4. Pesquisar animal por características")
    print("6. Sair")

def main():
    global animais_cadastrados, pessoas_interessadas
    animais_cadastrados = Fila()
    pessoas_interessadas = LinkedList()

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_animal()
        elif opcao == "2":
            cadastrar_pessoa()
        elif opcao == "3":
            gerar_relatorio()
        elif opcao == "4":
            pesquisar_animal()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
