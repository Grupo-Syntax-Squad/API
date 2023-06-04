from graficosSintomas_js import dados_internacoes
from graficosGastos_js import maioresgastos
from flask import Flask, render_template

DADOS_INTERNACOES = dados_internacoes()
DADOS_GASTOS = maioresgastos()
CAPSDESC = ['Doenças do sistema nervoso', 'Doenças do aparelho circulatório', 'Doenças do aparelho respiratório', 'Doenças do aparelho digestivo']
CORES = [
	'rgba(0, 0, 255)',
  	'rgba(50, 50, 255)',
    'rgba(100, 100, 255)',
    'rgba(150, 150, 255)',
  	'rgba(200, 200, 255)'     
]

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/index")
def home():
  return render_template('index.html')

@app.route("/acessomunicipio")
def acessomunicipio():
  return render_template('acessomunicipio.html')

@app.route("/acessoaparecida")
def acessoaparecida():
  return render_template('/municipios/acessoaparecida.html')

@app.route("/acessocaçapava")
def acessocaçapava():
  return render_template('/municipios/acessocaçapava.html')

@app.route("/acessojacarei")
def acessojacarei():
  return render_template('/municipios/acessojacarei.html')

@app.route("/acessosjc")
def acessosjc():
  return render_template('/municipios/acessosjc.html')

@app.route("/acessotaubate")
def acessotaubate():
  return render_template('/municipios/acessotaubate.html')

@app.route("/graficos_internacoes_sjc")
def graficos_internacoes_sjc():
  DADOS = DADOS_INTERNACOES["SJC"]
  return render_template('/municipios/graficos_internacoes_sjc.html', dados=DADOS, caps=CAPSDESC)

@app.route("/graficos_internacoes_aparecida")
def graficos_internacoes_aparecida():
  DADOS = DADOS_INTERNACOES["APARECIDA"]
  return render_template('/municipios/graficos_internacoes_aparecida.html', dados=DADOS, caps=CAPSDESC)

@app.route("/graficos_internacoes_cacapava")
def graficos_internacoes_cacapava():
  DADOS = DADOS_INTERNACOES["CACAPAVA"]
  return render_template('/municipios/graficos_internacoes_cacapava.html', dados=DADOS, caps=CAPSDESC)

@app.route("/graficos_internacoes_jacarei")
def graficos_internacoes_jacarei():
  DADOS = DADOS_INTERNACOES["JACAREI"]
  return render_template('/municipios/graficos_internacoes_jacarei.html', dados=DADOS, caps=CAPSDESC)

@app.route("/graficos_internacoes_taubate")
def graficos_internacoes_taubate():
  DADOS = DADOS_INTERNACOES["TAUBATE"]
  return render_template('/municipios/graficos_internacoes_taubate.html', dados=DADOS, caps=CAPSDESC)

@app.route("/graficos_consultas_taubate")
def graficos_consultas_taubate():
  return render_template('/municipios/graficos_consultas_taubate.html')

@app.route("/graficos_consultas_aparecida")
def graficos_consultas_aparecida():
  return render_template('/municipios/graficos_consultas_aparecida.html')

@app.route("/graficos_consultas_cacapava")
def graficos_consultas_cacapava():
  return render_template('/municipios/graficos_consultas_cacapava.html')

@app.route("/graficos_consultas_jacarei")
def graficos_consultas_jacarei():
  return render_template('/municipios/graficos_consultas_jacarei.html')

@app.route("/graficos_consultas_sjc")
def graficos_consultas_sjc():
  return render_template('/municipios/graficos_consultas_sjc.html')

@app.route("/graficos_medicamentos_taubate")
def graficos_medicamentos_taubate():
  return render_template('/municipios/graficos_medicamentos_taubate.html')

@app.route("/graficos_medicamentos_aparecida")
def graficos_medicamentos_aparecida():
  return render_template('/municipios/graficos_medicamentos_aparecida.html')

@app.route("/graficos_medicamentos_cacapava")
def graficos_medicamentos_cacapava():
  return render_template('/municipios/graficos_medicamentos_cacapava.html')

@app.route("/graficos_medicamentos_jacarei")
def graficos_medicamentos_jacarei():
  return render_template('/municipios/graficos_medicamentos_jacarei.html')

@app.route("/graficos_medicamentos_sjc")
def graficos_medicamentos_sjc():
  return render_template('/municipios/graficos_medicamentos_sjc.html')

@app.route("/graficos_gastos_sjc")
def graficos_gastos_sjc():
  GASTOS = DADOS_GASTOS['SJC']
  return render_template('/municipios/graficos_gastos_sjc.html', gastos=GASTOS, cores=CORES)

@app.route("/graficos_gastos_aparecida")
def graficos_gastos_aparecida():
  GASTOS = DADOS_GASTOS['Aparecida']
  return render_template('/municipios/graficos_gastos_aparecida.html', gastos=GASTOS, cores=CORES)

@app.route("/graficos_gastos_taubate")
def graficos_gastos_taubate():
  GASTOS = DADOS_GASTOS['Taubaté']
  return render_template('/municipios/graficos_gastos_taubate.html', gastos=GASTOS, cores=CORES)

@app.route("/graficos_gastos_jacarei")
def graficos_gastos_jacarei():
  GASTOS = DADOS_GASTOS['Jacareí']
  return render_template('/municipios/graficos_gastos_jacarei.html', gastos=GASTOS, cores=CORES)

@app.route("/graficos_gastos_cacapava")
def graficos_gastos_cacapava():
  GASTOS = DADOS_GASTOS['Caçapava']
  return render_template('/municipios/graficos_gastos_cacapava.html', gastos=GASTOS, cores=CORES)

@app.route("/quemsomos")
def quemsomos():
  return render_template('quemsomos.html')

@app.route("/diego")
def diego():
  nome = "Diego Dias"
  desc = "Olá, me chamo Diego Dias Motta, atualmente moro em Caçapava e faço parte da Developer Team da Syntax Squad. Nos tempos vagos gosto de Pescar e Viajar. Você pode ver mais sobre meus projetos acessando meu perfil no github. "
  img = "../../static/integrantes/diego.jpg"
  linkgit = "https://github.com/diegoboasorte"
  return render_template('/integrantes/baseintegrantes.html', nome=nome, desc=desc, img=img, linkgit=linkgit)

@app.route("/gabrieldeo")
def gabrieldeo():
  nome = "Gabriel Reis"
  desc = "Olá, me chamo Gabriel de Oliveira Silva Reis, atualmente moro em São José dos Campos, sou o Product Owner e faço parte da Developer Team da Syntax Squad. Nos tempos vagos gosto de jogar vídeo-game, praticar esportes e ouvir música. Você pode ver mais sobre meus projetos acessando meu perfil no GitHub. 😉"
  img = "../../static/integrantes/gabrieldeo.png"
  linkgit = "https://github.com/b4hia"
  return render_template('/integrantes/baseintegrantes.html', nome=nome, desc=desc, img=img, linkgit=linkgit)

@app.route("/gabrielf")
def gabrielf():
  nome = "Gabriel Felipe"
  desc = "Olá, me chamo Gabriel Felipe dos Santos, atualmente moro em São José dos Campos e faço parte da Developer Team da Syntax Squad. Nos tempos vagos gosto de jogar video game e assistir séries. Você pode ver mais sobre meus projetos acessando meu perfil no github. "
  img = "../../static/integrantes/gabrielf.png"
  linkgit = "https://github.com/gabrielfsantos99"
  return render_template('/integrantes/baseintegrantes.html', nome=nome, desc=desc, img=img, linkgit=linkgit)

@app.route("/joao")
def joao():
  nome = "João Vitor"
  desc = "Olá, me chamo João Vitor, atualmente moro em São José dos Campos e faço parte da Developer Team da Syntax Squad. Nos tempos vagos gosto de treinar e ler um livro. Você pode ver mais sobre meus projetos acessando meu perfil no GitHub. "
  img = "../../static/integrantes/joao.jpeg"
  linkgit = "https://github.com/JaovitoP"
  return render_template('/integrantes/baseintegrantes.html', nome=nome, desc=desc, img=img, linkgit=linkgit)

@app.route("/lucas")
def lucas():
  nome = "Lucas Langeani"
  desc = "Olá, me chamo Lucas Langeani, atualmente moro em São José dos Campos e faço parte da Developer Team da Syntax Squad. Nos tempos vagos gosto de tocar guitarra, ouvir música e praticar esportes. Você pode ver mais sobre meus projetos acessando meu perfil no GitHub. "
  img = "../../static/integrantes/lucas.png"
  linkgit = "https://github.com/langeanith"
  return render_template('/integrantes/baseintegrantes.html', nome=nome, desc=desc, img=img, linkgit=linkgit)

@app.route("/mateus")
def mateus():
  nome = "Mateus Reis"
  desc = "Olá, me chamo Mateus Reis, atualmente moro em São José dos Campos e faço parte da Developer Team da Syntax Squad. Nos tempos vagos gosto de trabalhos manuais, mecânica, jogos e uma cerveja gelada. Você pode ver mais sobre meus projetos acessando meu perfil no GitHub. "
  img = "../../static/integrantes/mateus.png"
  linkgit = "https://github.com/mhlreis"
  return render_template('/integrantes/baseintegrantes.html', nome=nome, desc=desc, img=img, linkgit=linkgit)

@app.route("/ryan")
def ryan():
  nome = "Ryan Araújo"
  desc = "Olá, me chamo Ryan Araújo, atualmente moro em São José dos Campos, sou o Scrum Master e faço parte da Developer Team da Syntax Squad. Nos tempos vagos gosto de . Você pode ver mais sobre meus projetos acessando meu perfil no GitHub. "
  img = "../../static/integrantes/ryan.jpg"
  linkgit = "https://github.com/ryanvdaraujo"
  return render_template('/integrantes/baseintegrantes.html', nome=nome, desc=desc, img=img, linkgit=linkgit)

@app.route("/wellington")
def wellington():
  nome = "Wellington Faria"
  desc = "Olá, me chamo Wellington, atualmente moro em São José dos Campos e faço parte do Dev Team da Syntax Squad. Nos tempos vagos gosto de jogar e realizar alguns projetos pessoais. Você pode ver mais sobre meus projetos acessando meu perfil no GitHub."
  img = "../../static/integrantes/wellington.jpg"
  linkgit = "https://github.com/WellingtonLFaria"
  return render_template('/integrantes/baseintegrantes.html', nome=nome, desc=desc, img=img, linkgit=linkgit)
