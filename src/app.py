
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/index.html")
def home():
  return render_template('index.html')

@app.route("/acessomunicipio.html")
def acessomunicipio():
  return render_template('acessomunicipio.html')

@app.route("/municipios/acessoaparecida.html")
def acessoaparecida():
  return render_template('/municipios/acessoaparecida.html')

@app.route("/municipios/acessocaçapava.html")
def acessocaçapava():
  return render_template('/municipios/acessocaçapava.html')

@app.route("/municipios/acessojacarei.html")
def acessojacarei():
  return render_template('/municipios/acessojacarei.html')

@app.route("/municipios/acessosjc.html")
def acessosjc():
  return render_template('/municipios/acessosjc.html')

@app.route("/municipios/acessotaubate.html")
def acessotaubate():
  return render_template('/municipios/acessotaubate.html')

@app.route("/quemsomos.html")
def quemsomos():
  return render_template('quemsomos.html')

@app.route("/integrantes/diego.html")
def diego():
  return render_template('/integrantes/diego.html')

@app.route("/integrantes/gabrieldeo.html")
def gabrieldeo():
  return render_template('/integrantes/gabrieldeo.html')

@app.route("/integrantes/gabrielf.html")
def gabrielf():
  return render_template('/integrantes/gabrielf.html')

@app.route("/integrantes/joao.html")
def joao():
  return render_template('/integrantes/joao.html')

@app.route("/integrantes/lucas.html")
def lucas():
  return render_template('/integrantes/lucas.html')

@app.route("/integrantes/mateus.html")
def mateus():
  return render_template('/integrantes/mateus.html')

@app.route("/integrantes/ryan.html")
def ryan():
  return render_template('/integrantes/ryan.html')

@app.route("/integrantes/wellington.html")
def wellington():
  return render_template('/integrantes/wellington.html')