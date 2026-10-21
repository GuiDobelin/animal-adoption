<h1 align="center">🐾 Animal Adoption</h1>

<p align="center">
  Sistema de terminal para a prefeitura cadastrar animais para adoção e pessoas interessadas, cruzando espécies e preferências.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Estrutura_de_Dados-Fila_·_Pilha_·_Lista_Encadeada-6E40C9?style=flat-square" alt="Estruturas de dados">
  <img src="https://img.shields.io/badge/Projeto-Acadêmico-orange?style=flat-square" alt="Projeto acadêmico">
</p>

---

## 📖 Sobre

Projeto feito na disciplina de **Estrutura de Dados**, no 3º período de **Engenharia de Software**, com o professor [Marcio Garrido](https://github.com/marciogarridoLaCop).

### Enunciado

> A prefeitura precisa de um sistema para cadastrar animais **por tipo** (canino, felino etc.), permitindo incluir novos tipos dinamicamente, classificados por **idade aproximada, cor, porte e particularidades**. O sistema também cadastra **pessoas interessadas** na adoção, com contato, espécie desejada e preferências. No fim do mês a prefeitura emite um **relatório cruzando animais disponíveis e candidatos**, e o atendente pode **pesquisar animais** pelas características pedidas por quem liga.

## ✨ Funcionalidades

- 🐶 **Cadastro de animais**: tipo, idade, cor, porte e particularidade
- 🙋 **Cadastro de adotantes**: nome, telefone, espécie de interesse e preferência
- 📋 **Relatório de cruzamento** entre animais disponíveis e candidatos
- 🔎 **Pesquisa de animais** por características

## 🧠 Estruturas de dados usadas

| Estrutura | Implementação |
|---|---|
| Lista encadeada | `LinkedList` / `Node` |
| Fila (FIFO) | `Fila` |
| Pilha (LIFO) | `Pilha` |

## ▶️ Como executar

**Pré-requisito:** Python 3 instalado (não há dependências externas).

```bash
git clone https://github.com/GuiDobelin/animal-adoption.git
cd animal-adoption
python3 main.py
```

## 🖥️ Demonstração

**Menu principal**

![Menu](https://github.com/GuiDobelin/animal-adoption/assets/105359316/7ad50256-18fc-4220-87b1-8cac03083e01)

<details>
<summary><b>Ver mais telas</b></summary>

**Cadastro de animal**

![Cadastro de animal](https://github.com/GuiDobelin/animal-adoption/assets/105359316/076070fd-7f22-4c8c-8f8a-439d32a65564)

**Cadastro de pessoa**

![Cadastro de pessoa](https://github.com/GuiDobelin/animal-adoption/assets/105359316/cd47ff6c-cc17-4029-b465-0ddfc2f00d0a)

**Relatório de cruzamento**

![Relatório](https://github.com/GuiDobelin/animal-adoption/assets/105359316/6b5e7798-a73f-42c8-bae1-900ec8598f5f)

**Pesquisa por características**

![Pesquisa](https://github.com/GuiDobelin/animal-adoption/assets/105359316/d5bd559e-214e-4710-8505-7ce9521bcf53)

</details>

## 🔀 Fluxograma

![Fluxograma](https://github.com/GuiDobelin/animal-adoption/assets/105359316/54121c37-a8c2-4185-8d55-053fa9927d7d)

📄 [Fluxograma em PDF](https://github.com/GuiDobelin/animal-adoption/files/11727899/sodapdf-converted.pdf)

## 📁 Estrutura

```
animal-adoption/
├── main.py      # Menu, estruturas de dados, cadastro, relatório e pesquisa
├── animal.py    # Classe Animal
└── pessoa.py    # Classe Pessoa
```

---

<p align="center">Feito por <a href="https://github.com/GuiDobelin">Guilherme Dobelin</a></p>
