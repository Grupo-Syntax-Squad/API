import os
import pandas as pd
import plotly.express as px

MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
ANOS = ["2019", "2020", "2021", "2022"]

valoresanos = []

for ano in ANOS:
    valores = []
    df = pd.read_excel(f'{os.getcwd()}/Gastos{ano}/{ano}.xlsx')
    total = df.sort_values('Quanto já foi realizado <br>(Empenhado ou Pago)')
    total.reset_index(drop=True, inplace=True)
    for valor in total['Quanto já foi realizado <br>(Empenhado ou Pago)'][-5:]:
        valores.append(valor)
    valoresanos.append(sorted(valores, reverse=True))

if os.path.exists(f"5maioresgastos.csv"):
    os.remove(f"5maioresgastos.csv")

with open("5maioresgastos.csv", "a") as arquivo:
    for ano in valoresanos:
        arquivo.write(f"{ano}\n")

valoresanos = pd.DataFrame(valoresanos, index=ANOS)

fig = px.bar(valoresanos, text_auto=True, barmode="group", width=700, height=600, title="5 maiores gastos por ano de Caçapava", labels={
                     "value": "Gastos (R$)",
                     "index": "Anos"
                 })

fig.update_layout(showlegend=False, title_x=0.5)
fig.update_traces(textposition="inside")

fig.show()

fig.write_image(f'{os.getcwd()}/GráficoGastosporAnoCaçapava.svg')