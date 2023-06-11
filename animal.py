from main import *

class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

def cadastrar_animal():
    tipo = input("Tipo do animal: ")
    idade = input("Idade aproximada do animal: ")
    cor = input("Cor do animal: ")
    porte = input("Porte do animal: ")
    particularidade = input("Particularidade do animal: ")

    animal = Animal(tipo, idade, cor, porte, particularidade)
    animais_cadastrados.enfileirar(animal)
    print("Animal cadastrado com sucesso!")

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
