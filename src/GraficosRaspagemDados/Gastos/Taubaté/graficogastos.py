import plotly.express as px
import pandas as pd
import os

anos = ["2019", "2020", "2021", "2022"]
valores = []
for ano in anos:
    valoresano =[]
    with open(f"{os.getcwd()}/os5maioresgastos{ano}.csv") as arquivo:
        for linha in arquivo.readlines():
            valoresano.append(float(linha))
        valoresano.pop(0)
        valores.append(valoresano)

if os.path.exists(f"5maioresgastos.csv"):
    os.remove(f"5maioresgastos.csv")

with open("5maioresgastos.csv", "a") as arquivo:
    for ano in valores:
        arquivo.write(f"{ano}\n")

df = pd.DataFrame(valores, index=anos)

fig = px.bar(df, text_auto=True, barmode="group", width=700, height=600, title="5 maiores gastos por ano de Taubaté", labels={
                     "value": "Gastos (R$)",
                     "index": "Anos"
                 })

fig.update_layout(showlegend=False)
fig.update_layout(title_x=0.5)
fig.write_image(f"{os.getcwd()}/GráficoGastosporAnoTaubate.svg")

fig.show()
