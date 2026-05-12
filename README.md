🇧🇷 **Português** | 🇺🇸 [English](README-eng.md)
<H1> Trabalho de Algoritmos de Ordenação - Sistema de Biblioteca (SB) 📚 </H1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Concluido-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Ordenação-Quick%20%7C%20Heap%20%7C%20Radix-purple?style=flat-square" alt="Ordenação"></p>

<p align="center">
  <img src="https://i.postimg.cc/YCsvxJLN/Captura-de-Tela-2026-04-04-a-s-02-39-39.png" width="500">
</p>

---

## 📹 Vídeo explicando o projeto 
[Vídeo do youtube](https://youtu.be/dPdShpI-ZTY)


## 📝 Descrição

O **Sistema de Biblioteca (SB)** é uma aplicação em Python pensada para ser rápida e fácil de usar. Com uma interface moderna em modo escuro, ele foi projetado para que a navegação e a organização do acervo aconteçam de forma fluida, sem travamentos ou esperas desnecessárias.

Nesta nova versão, o foco principal do sistema é a **estruturação e ordenação dinâmica dos dados**. Para lidar com diferentes tipos de informações (textos, números inteiros, valores decimais e datas), o sistema aplica abordagens específicas para cada coluna da tabela. Isso inclui o uso de **Quick Sort** para categorização alfabética, **Heap Sort** para ranqueamento preciso de notas e **Radix Sort (MSD)** para ordenação cronológica.

No fim, o sistema consegue listar, reorganizar e inverter grandes quantidades de livros instantaneamente, mantendo um equilíbrio perfeito entre eficiência algorítmica e uma experiência de uso simples e agradável no dia a dia.

## 💡 Diferenciais Técnicos (Algoritmos de Ordenação)

O grande destaque desta atualização é o Módulo de Ordenação, que utiliza diferentes estratégias algorítmicas dependendo da coluna selecionada pelo usuário na interface:

- **Quick Sort:** Implementado como o algoritmo principal (faz-tudo) para ordenação de *strings* (Título, Autor, Gênero) e inteiros simples (Numeração de ID e Quantidade de Empréstimos). Garante velocidade na organização alfabética e por popularidade.
- **Heap Sort:** Estruturado especificamente para organizar os livros baseando-se em números de ponto flutuante (*floats*). É disparado quando o usuário deseja visualizar as maiores ou menores Notas Médias de avaliação do acervo.
- **Radix Sort (MSD):** Implementado com a abordagem recursiva *Most Significant Digit* utilizando a separação em *buckets* (baldes). É o algoritmo ideal para ordenação de números inteiros de tamanho fixo, sendo aplicado exclusivamente para ordenar os Anos de Publicação.
- **Merge Sort:** Algoritmo de divisão e conquista implementado na biblioteca principal do sistema, garantindo flexibilidade e estabilidade como alternativa base para processamento de dados.

## 🌐 Demonstração da Ordenação

<p align="center">
  <img src="https://i.postimg.cc/SQrYLNBB/image.png" width="600">
  <br></br>
  <img src="https://i.postimg.cc/nVRccjbv/image.png" width="600">
  <br></br>
  <img src="https://i.postimg.cc/tJwjd6pS/image.png" width="600">
</p>

## 🎯 Funcionalidades

- **Ordenação Dinâmica em Tabela:** Clique em qualquer cabeçalho da tabela de livros para organizar o acervo instantaneamente, com suporte a ordenação reversa (Crescente/Decrescente ou A-Z/Z-A).
- **Gestão de Acervo:** Cadastro detalhado de livros, com título, autor, gênero e estoque.
- **Registro de Alunos:** Controle centralizado de usuários, armazenando matrículas e dados de contato de forma segura.
- **Edição Dinâmica:** Permite alterar informações de livros e alunos já cadastrados, mantendo a base de dados sempre atualizada.
- **Controle de Empréstimos e Popularidade:** Registro ágil de saídas, associando o aluno ao livro e contabilizando automaticamente a quantidade de vezes que a obra foi emprestada.
- **Gestão de Devoluções e Avaliações:** Baixa automática de empréstimos com a funcionalidade integrada para o aluno registrar uma avaliação de 0 a 5 estrelas para a obra devolvida.

---

## 💻 Pré-requisitos

Antes de executar o programa, certifique-se de que você possui os seguintes requisitos instalados:

**1. Python 3.10 ou superior.**

**2. Dependências:**

- PySide6; e 
- qdarktheme.

**3.Sistema Operacional: Windows, macOS ou Linux.**

 ---

## 🚀 Executando

**1. Instalar o python**

Verifique se você possui o **Python 3.10 ou superior** instalado em seu sistema. Para isso, siga as instruções abaixo:

Abra o Terminal (no Windows, você pode abrir o Prompt de Comando ou PowerShell).

Digite o seguinte comando para verificar a versão do Python:

```bash
python --version
```

**Ou**

```bash
python3 --version
```

Se não tiver o Python 3.10, você pode baixá-lo [aqui](https://www.python.org/downloads/).

**2. Clonar o Repositório**

Primeiro, clone o repositório do projeto para a sua máquina. Para isso, abra o terminal (ou prompt de comando no Windows) e execute o comando abaixo:

```bash
git clone https://github.com/eda2-2026/G41_Ordenacao_EDA2-2026.1.git
```

**3. Instale as dependências:**

No terminal, navegue até o diretório onde o projeto foi baixado e execute o seguinte comando para instalar todas as dependências:

```bash
pip install -r requirements.txt
```

Se o arquivo **requirements.txt** não existir, você pode instalar as dependências manualmente.
- **Instalar o Pyside6**

```bash
pip install pyside6 
```

* **Instalar o qdarktheme**

```bash
pip install qdarktheme
```

**4. Executar o programa**

Com o ambiente configurado e as dependências instaladas, agora você pode rodar o sistema.

```bash
python biblioteca.py
```

Ou

```bash
python3 biblioteca.py
```

**⚠️ Observação:**
Caso o código apresente algum erro durante a execução, verifique se todos os arquivos necessários estão presentes (principalmente os arquivos .json no diretório db_files).

---

## 🫂 Colaboradores

| <span style="color:black;">[Camila Cavalcante - 232013944](https://github.com/CamilaSilvaC)</span> | <span style="color:black;">[Luísa Ferreira - 232014807](https://github.com/luisa12ll)</span> |
| :---: | :---: |
| <div align="center"><img src="https://github.com/CamilaSilvaC.png" alt="camila" width="400"></div> | <div align="center"><img src="https://github.com/luisa12ll.png" alt="luisa" width="400"></div> |
