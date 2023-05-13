# ***Raspagem de Dados***

## **Como foi realizada a raspagem**

A raspagem de dados foi realizada utilizando a biblioteca Selenium que permite automatizar ações e coletar informações através dos navegadores suportados pela biblioteca.

**O navegador utilizado foi o [Chrome](https://www.google.com/intl/pt-BR/chrome/).**

## **Scripts em que a raspagem de dados foi realizada**

- [Script para raspagem dos dados de gastos gerais de São José dos Campos](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/SJC/raspagemgastos.py).

## **Executando os Scripts de raspagem**

### **Criando e ativando o ambiente virtual (OPCIONAL)**

Caso deseje utilizar um ambiente virtual para instalar as bibliotecas no mesmo digite os seguintes comandos no terminal:

    cd .\src\ | python -m venv venv
    .\venv\Scripts\activate

### **Instalando as bibliotecas necessárias**

Para rodar os scripts de raspagem é necessário instalar as bibliotecas que realizam esse processo.

Para isso abra o terminal e digite o seguinte comando:

    cd '.\src\Gráficos e Raspagem de Dados\' | pip install -r .\requirements.txt

### **Executar o Script de raspagem**

Após ter instalado as bibliotecas necessárias apenas execute o Script que tenha raspagem.

    python caminho/do/arquivo/script_raspagem.py

---

# ***Gráficos***

## **Como foram feitos**

Os gráficos foram feitos utilizando a biblioteca Plotly para confecção de gráficos e foram salvos em formato [.svg](https://www.adobe.com/br/creativecloud/file-types/image/vector/svg-file.html#:~:text=SVG%3A%20perguntas%20frequentes-,O%20que%20%C3%A9%20um%20arquivo%20SVG%3F,e%20linhas%20em%20uma%20grade.).

## **Scripts que foram usados para fazer os gráficos**

- [Script para confecção do gráfico dos 5 maiores gastos de Aparecida](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/Aparecida/graficogastos.py).

- [Script para confecção do gráfico dos 5 maiores gastos de Caçapava](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/Ca%C3%A7apava/graficogastos.py).

- [Script para confecção do gráfico dos 5 maiores gastos de Jacareí](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/Jacare%C3%AD/graficogastos.py).

- [Script para confecção do gráfico dos 5 maiores gastos de São José dos Campos](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/SJC/graficogastos.py).

- [Script para confecção do gráfico dos 5 maiores gastos de Taubaté](https://github.com/GRUPOAPIDSM2023/API/blob/main/src/Gr%C3%A1ficos%20e%20Raspagem%20de%20Dados/Gastos/Taubat%C3%A9/graficogastos.py).