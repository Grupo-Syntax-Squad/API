from graficosSintomas_js import dados_internacoes
from graficosGastos_js import maioresgastos
from flask import Flask, render_template

DADOS_INTERNACOES = dados_internacoes()
DADOS_GASTOS = maioresgastos()

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
  return render_template('/municipios/graficos_internacoes_sjc.html', dados=DADOS)

@app.route("/graficos_internacoes_aparecida")
def graficos_internacoes_aparecida():
  DADOS = DADOS_INTERNACOES["APARECIDA"]
  return render_template('/municipios/graficos_internacoes_aparecida.html', dados=DADOS)

@app.route("/graficos_internacoes_cacapava")
def graficos_internacoes_cacapava():
  DADOS = DADOS_INTERNACOES["CACAPAVA"]
  return render_template('/municipios/graficos_internacoes_cacapava.html', dados=DADOS)

@app.route("/graficos_internacoes_jacarei")
def graficos_internacoes_jacarei():
  DADOS = DADOS_INTERNACOES["JACAREI"]
  return render_template('/municipios/graficos_internacoes_jacarei.html', dados=DADOS)

@app.route("/graficos_internacoes_taubate")
def graficos_internacoes_taubate():
  DADOS = DADOS_INTERNACOES["TAUBATE"]
  return render_template('/municipios/graficos_internacoes_taubate.html', dados=DADOS)

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
  return render_template('/municipios/graficos_gastos_sjc.html', gastos=GASTOS)

@app.route("/graficos_gastos_aparecida")
def graficos_gastos_aparecida():
  GASTOS = DADOS_GASTOS['Aparecida']
  return render_template('/municipios/graficos_gastos_aparecida.html', gastos=GASTOS)

@app.route("/graficos_gastos_taubate")
def graficos_gastos_taubate():
  GASTOS = DADOS_GASTOS['Taubaté']
  return render_template('/municipios/graficos_gastos_taubate.html', gastos=GASTOS)

@app.route("/graficos_gastos_jacarei")
def graficos_gastos_jacarei():
  GASTOS = DADOS_GASTOS['Jacareí']
  return render_template('/municipios/graficos_gastos_jacarei.html', gastos=GASTOS)

@app.route("/graficos_gastos_cacapava")
def graficos_gastos_cacapava():
  GASTOS = DADOS_GASTOS['Caçapava']
  return render_template('/municipios/graficos_gastos_cacapava.html', gastos=GASTOS)

@app.route("/quemsomos")
def quemsomos():
  return render_template('quemsomos.html')

@app.route("/diego")
def diego():
  return render_template('/integrantes/diego.html')

@app.route("/gabrieldeo")
def gabrieldeo():
  return render_template('/integrantes/gabrieldeo.html')

@app.route("/gabrielf")
def gabrielf():
  return render_template('/integrantes/gabrielf.html')

@app.route("/joao")
def joao():
  return render_template('/integrantes/joao.html')

@app.route("/lucas")
def lucas():
  return render_template('/integrantes/lucas.html')

@app.route("/mateus")
def mateus():
  return render_template('/integrantes/mateus.html')

@app.route("/ryan")
def ryan():
  return render_template('/integrantes/ryan.html')

@app.route("/wellington")
def wellington():
  return render_template('/integrantes/wellington.html')