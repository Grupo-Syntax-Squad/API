
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

@app.route("/acessoaparecida.html")
def acessoaparecida():
  return render_template('acessoaparecida.html')

@app.route("/acessocaçapava.html")
def acessocaçapava():
  return render_template('acessocaçapava.html')

@app.route("/acessojacarei.html")
def acessojacarei():
  return render_template('acessojacarei.html')

@app.route("/acessosjc.html")
def acessosjc():
  return render_template('acessosjc.html')

@app.route("/acessotaubate.html")
def acessotaubate():
  return render_template('acessotaubate.html')

@app.route("/quemsomos.html")
def quemsomos():
  return render_template('quemsomos.html')