from main import *

class Pessoa:
    def __init__(self, nome, telefone, especie_interesse, preferencia_animal):
        self.nome = nome
        self.telefone = telefone
        self.especie_interesse = especie_interesse
        self.preferencia_animal = preferencia_animal
        
def cadastrar_pessoa():
    nome = input("Nome da pessoa: ")
    telefone = input("Telefone da pessoa: ")
    especie_interesse = input("Espécie de interesse para adoção: ")
    preferencia_animal = input("Preferência de animal: ")
