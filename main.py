class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade
        
class Pessoa:
    def __init__(self, nome, telefone, especie_interesse, preferencia_animal):
        self.nome = nome
        self.telefone = telefone
        self.especie_interesse = especie_interesse
        self.preferencia_animal = preferencia_animal
        
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
    
    def pop(self):
        if self.vazia():
            return None
        return self.items.pop()
    
    def tamanho(self):
        return len(self.items)

def cadastrar_animal():
    tipo = input("Tipo do animal: ")
    idade = input("Idade aproximada do animal: ")
    cor = input("Cor do animal: ")
    porte = input("Porte do animal: ")
    particularidade = input("Particularidade do animal: ")
    
    animal = Animal(tipo, idade, cor, porte, particularidade)
    animais_cadastrados.enfileirar(animal)
    print("Animal cadastrado com sucesso!")

def cadastrar_pessoa():
    nome = input("Nome da pessoa: ")
    telefone = input("Telefone da pessoa: ")
    especie_interesse = input("Espécie de interesse para adoção: ")
    preferencia_animal = input("Preferência de animal: ")

    pessoa = Pessoa(nome, telefone, especie_interesse, preferencia_animal)
    pessoas_interessadas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def gerar_relatorio():
    especie = input("Espécie de animal: ")
    candidatos = [pessoa for pessoa in pessoas_interessadas if pessoa.especie_interesse == especie]

    print("Candidatos para adoção da espécie", especie)
    for candidato in candidatos:
        print("Nome:", candidato.nome)
        print("Telefone:", candidato.telefone)
        print("Preferência de animal:", candidato.preferencia_animal)
        print()

def pesquisar_animal():
    caracteristicas = input("Características do animal: ")

    for animal in animais_cadastrados.items:
        if caracteristicas.lower() in animal.tipo.lower():
            print("Animal encontrado:")
            print("Tipo:", animal.tipo)
            print("Idade:", animal.idade)
            print("Cor:", animal.cor)
            print("Porte:", animal.porte)
            print("Particularidade:", animal.particularidade)
            return
        
    print("Nenhum animal encontrado com as características informadas.")

def pesquisa_binaria(lista, valor, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == valor:
        return meio
    elif lista[meio] < valor:
        return pesquisa_binaria(lista, valor, meio + 1, fim)
    else:
        return pesquisa_binaria(lista, valor, inicio, meio - 1)
    
def exibir_menu():
    print("1. Cadastrar animal")
    print("2. Cadastrar pessoa interessada")
    print("3. Gerar relatório de candidatos para adoção")
    print("4. Pesquisar animal por características")
    print("5. Pesquisa binária em lista de animais")
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
            lista_animais = [animal.tipo for animal in animais_cadastrados.items]
            lista_animais.sort()
            
            valor = input("Tipo do animal a pesquisar: ")
            resultado = pesquisa_binaria(lista_animais, valor, 0, len(lista_animais) - 1)
            if resultado != -1:
                print("Animal encontrado:", lista_animais[resultado])
            else:
                print("Animal não encontrado.")
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()
