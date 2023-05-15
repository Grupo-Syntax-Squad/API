# 📊**Raspagem de Dados**

## 🤔**Como foi realizada a raspagem**

A raspagem de dados foi realizada utilizando a biblioteca Selenium que permite automatizar ações e coletar informações através dos navegadores suportados pela biblioteca.

Vídeo demonstrativo da raspagem de gastos gerais de São José dos Campos:

https://github.com/GRUPOAPIDSM2023/API/assets/91472871/9c41b1c0-9a4c-4c4e-a346-9ac1cb232d17

**O navegador utilizado foi o [Chrome](https://www.google.com/intl/pt-BR/chrome/).**

## **Scripts em que a raspagem de dados foi realizada**

- [Script para raspagem dos dados de gastos gerais de São José dos Campos](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/SJC/raspagemgastos.py).

## 🔌**Executando os Scripts de raspagem**

### Requisitos:

Para que a executar o script da raspagem, listamos um passo a passo para guiar o usuário:

1. Intalação do Git:
  - Você precisará do git instalado para poder fazer a clonagem deste repositório; [Clique aqui para instalar o Git](https://git-scm.com/downloads). 

2. 🐍Python:
  - No momento em que for instalar o python, escolha uma versão superior à 3.6. Durante a instalação, não se esqueça de marcar a opção da instalação do "pip"; [Clique aqui para instalar o python](https://www.python.org/downloads/).

### Clonando o repositório

Com o Git e o Python instalados em sua máquina, siga os próximos passos:

1. Clone o repositório através de um terminal, utilize o comando:

```
git clone https://github.com/GRUPOAPIDSM2023/API.git
``` 

### **Criando e ativando o ambiente virtual (OPCIONAL)**

Caso deseje utilizar um ambiente virtual para instalar as bibliotecas, digite os seguintes comandos no terminal:

```bash
cd ./src/ | python -m venv venv | ./venv/Scripts/activate
```

### **Instalando as bibliotecas necessárias**

Para rodar os scripts de raspagem é necessário instalar as bibliotecas que realizam esse processo.

Para isso abra o terminal e digite o seguinte comando:

```bash
cd '.\src\Gráficos e Raspagem de Dados\' | pip install -r ./requirements.txt
```

### **Executar o Script de raspagem**

Após ter instalado as bibliotecas necessárias apenas execute o Script que tenha raspagem.

```bash
python caminho/do/arquivo/script_raspagem.py
```

---

# 📊**Gráficos**

## 🤔**Como foram feitos**

Os gráficos foram feitos utilizando a biblioteca Plotly para confecção de gráficos e foram salvos em formato [.svg](https://www.adobe.com/br/creativecloud/file-types/image/vector/svg-file.html#:~:text=SVG%3A%20perguntas%20frequentes-,O%20que%20%C3%A9%20um%20arquivo%20SVG%3F,e%20linhas%20em%20uma%20grade.).

## 🔧**Scripts que foram usados para fazer os gráficos**

- [Script para confecção do gráfico dos 5 maiores gastos de Aparecida](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/Aparecida/graficogastos.py).

- [Script para confecção do gráfico dos 5 maiores gastos de Caçapava](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/Ca%C3%A7apava/graficogastos.py).

- [Script para confecção do gráfico dos 5 maiores gastos de Jacareí](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/Jacare%C3%AD/graficogastos.py).

- [Script para confecção do gráfico dos 5 maiores gastos de São José dos Campos](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/SJC/graficogastos.py).

- [Script para confecção do gráfico dos 5 maiores gastos de Taubaté](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/Taubat%C3%A9/graficogastos.py).
