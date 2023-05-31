import pandas as pd
import os
import plotly.express as px
from pprint import pprint

MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
ANOS = ["2019", "2020", "2021", "2022"]

valoresanos = []

for ano in ANOS:
    valores = []
    df = pd.read_csv(f'{os.getcwd()}/Gastos{ano}/detalhamentoDespesas{ano}.csv', sep=';') 
    total = df.sort_values('vl_total_pag')
    total.reset_index(drop=True, inplace=True)
    for valor in total['vl_total_pag'][-5:]:
        valores.append(valor)
    valoresanos.append(sorted(valores, reverse=True))

if os.path.exists(f"5maioresgastos.csv"):
    os.remove(f"5maioresgastos.csv")

with open("5maioresgastos.csv", "a") as arquivo:
    for ano in valoresanos:
        arquivo.write(f"{ano}\n")

valoresanos = pd.DataFrame(valoresanos, index=ANOS)

fig = px.bar(valoresanos, text_auto=True, barmode="group", width=700, height=600, title="5 maiores gastos por ano de Jacareí", labels={
                     "value": "Gastos (R$)",
                     "index": "Anos"
                 })

fig.update_layout(showlegend=False, title_x=0.5)
fig.update_traces(textposition="inside")

fig.show()

fig.write_image(f'{os.getcwd()}/GráficoGastosporAnoJacarei.svg')