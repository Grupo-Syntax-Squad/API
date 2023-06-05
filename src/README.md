# 🤔Como Utilizar nosso Site:

## Requisitos

Para que a execução do sistema e seu uso sejam efetivados, listamos um passo a passo para realizar guiar o usuário:

1. Intalação do Git:
  - Você precisará do git instalado para poder fazer a clonagem deste repositório; [Clique aqui para instalar o Git](https://git-scm.com/downloads). 

2. Python:
  - No momento em que for instalar o python, escolha uma versão superior à 3.6. Durante a instalação, não se esqueça de marcar a opção da instalação do "pip"; [Clique aqui para instalar o python](https://www.python.org/downloads/).

3. Docker:
  -Você também precisará instalar o Docker. Faça o download da versão mais recente disponível: <br>
      [Clique aqui para instalar o Docker para Windowns](https://docs.docker.com/desktop/install/windows-install/).</br>
      [Clique aqui para instalar o Docker para MAC](https://docs.docker.com/desktop/install/mac-install/)</br>
      [Clique aqui para instalar o Docker para Linus(Ubuntu)](https://docs.docker.com/engine/install/ubuntu/)</br>
      
  -3.2 Instale o plugin do Docker compose seguindo as instruções para seu SO de acordo com as instruções disponíveis em: [Docker Compose](https://docs.docker.com/compose/install/)

## Clonando o repositório

Com o Git, Python e Docker devidamente instalados em sua máquina, siga os próximos passos:

1. Clone o repositório através de um terminal, utilize o comando:

```
git clone https://github.com/GRUPOAPIDSM2023/API.git
``` 

2. Ainda no terminal vá para a pasta src:
```
cd API/
cd src/
```
3. Execute o comando:
```
docker compose up
```
este comando irá fazer o biuld a imagem do sistema que inicializará o container automaticamente;

4. Basta acessar o endereço no seu navegador de preferência para ter acesso ao sistema funcionando:
```
localhost:5000
```
## Iniciando o ambiente virtual
- caso queira você pode rodar a aplicação sem usar o docker seguindo os seguintes passos:

Com o repositório clonado e no diretório correto, você deverá criar um ambiente virtual para rodar o sistema. Siga os próximos passos:

1. Ao entrar na pasta src, digite os seguintes comandos:
```
py -3 -m venv venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
flask run
```

> O comando flask run, irá inicializar o site dentro do ambiente virtual.
> Provavelmente irá aparecer um link no próprio terminal, basta segurar a tecla "CONTROL" e clicar sobre o link ou então simplesmente acessar no seu navegador o link: http://127.0.0.1:5000

## Desativando o ambiente

Para encerrar o uso do site e sair do ambiente virtual vá ao seu terminal, (onde o Flask está rodando) aperte a tecla CONTROL, em seguida a tecla "C" e execute o seguinte comando no terminal:
```
deactivate
```

## Vídeo Demonstrativo do Site Funcionando (Versão Atual):
> O vídeo abaixo é um exemplo do site em funcionamento.


https://github.com/GRUPOAPIDSM2023/API/assets/125401155/af9d359d-d948-475b-8054-29a1184abea2
