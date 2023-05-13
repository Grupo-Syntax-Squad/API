import plotly.express as px
import pandas as pd
import pprint

anos = ["2019", "2020", "2021", "2022"]
valores = []
for ano in anos:
    print(ano)
    valoresano =[]
    with open(f"src/Gráficos e Raspagem de Dados/Gastos/Taubaté/os5maioresgastos{ano}.csv") as arquivo:
        for linha in arquivo.readlines():
            print(linha, end="")
            valoresano.append(float(linha))
        valoresano.pop(0)
        valores.append(valoresano)

pprint.pprint(valores)

df = pd.DataFrame(valores, index=anos)

print(df)

fig = px.bar(df, text_auto=True, barmode="group", width=700, height=600, title="5 maiores gastos por ano de Taubaté", labels={
                     "value": "Gastos (R$)",
                     "index": "Anos"
                 })

fig.update_layout(showlegend=False)
fig.update_layout(title_x=0.5)
fig.write_image(f"src/Gráficos e Raspagem de Dados/Gastos/Taubaté/GráficoGastosporAnoTaubate.svg")

fig.show()
