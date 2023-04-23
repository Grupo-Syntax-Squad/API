# 🤔Como Utilizar nosso Site:

## Requisitos

Para que a execução do sistema e seu uso sejam efetivados, listamos um passo a passo para realizar guiar o usuário:

1. Intalação do Git:
  - Você precisará do git instalado para poder a clonagem deste repositório; [Clique aqui para instalar o Git](https://git-scm.com/downloads). 

2. Python:
  - No momento em que for instalar o python, escolha uma versão superior à 3.6. Durante a instalação, não se esqueça de marcar a opção da instalação do "pip"; [Clique aqui para instalar o python](https://www.python.org/downloads/).

## Clonando o repositório

Com o Git e o Python instalados em sua máquina, siga os próximos passos:

1. Clone o repositório através de um terminal, utilize o comando:

```
git clone https://github.com/GRUPOAPIDSM2023/API.git
``` 

2. Ainda no terminal vá para a pasta src:
```
cd API/
cd src/
```

## Iniciando o ambiente virtual

Com o repositório clonado e no diretório correto, você deverá criar um ambiente virtual para rodar o sistema: siga os próximos passos:

1. Ao entrar na pasta src, digite os seguintes comandos:
```
py -3 -m venv venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
flask run
```

> O comando flask run, irá inicializar o site dentro do ambiente virtual.
> Provavelmente irá aparecer um link no próprio terminal, basta segurar a tecla "CONTROL" e clicar sobre o link ou então simplesmente acesse este: http://127.0.0.1:5000

## Desativando o ambiente

Para encerrar o uso do site e sair do ambiente virtual, execute o seguinte comando no terminal:
```
deactivate
```
